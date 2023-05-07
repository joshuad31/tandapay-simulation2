import copy
import os
import shutil
import time
from datetime import datetime
import random
from settings import RESULT_DIR
from utils.logger import logger


class TandaPaySimulatorV2(object):

    def __init__(self, ev=None, pv=None, count=10, bundling=0, matrix=False):
        self.ev = ev or {}
        self.cov_req = ev['total_member_cnt'] * 0.025 * ev['monthly_premium']
        self._total = ev['total_member_cnt']
        self.pv = pv or {}
        self.period = 0
        self.matrix = matrix
        self.bundling = bundling
        self.count = count
        self._u_d = [
            {
                'orig_sbg_num': 0,
                'remaining_orig_sbg': 0,
                'cur_sbg_num': 0,
                'members_cur_sbg': 0,
                'sbg_status': 'valid',
                'sbg_reorg_cnt': 0,
                'pri_role': '',
                'sec_role': '',
                'cur_status': 'paid',
                'reorged_cnt': 0,
                'payable': 'yes',
                'defector_cnt': 0,
                'cur_month_balance': 0,
                'cur_month_premium': 0,
                'cur_month_1st_calc': 0,
                'cur_month_sec_cals': [0, ] * count,
                'total_value_refunds': [0, ] * count,
                'wallet_balance': 0,
                'wallet_claim_award': 0,
                'wallet_no_claim_refund': 0,
                'wallet_reorg_refund': 0,
                'credit_to_savings_account': 0,
                'prior_premiums': [0] * self.bundling,
                'debit_to_savings_account': [0, ] * count,
            } for _ in range(ev['total_member_cnt'])]

        self._s_d = [
            {
                'valid_remaining': ev['total_member_cnt'],
                'defected_cnt': 0,
                'skipped_cnt': 0,
                'invalid_cnt': 0,
                'quit_cnt': 0,
                'reorged_cnt': 0,
                'defection_shortfall': 0,
                'skip_shortfall': 0,
                'invalid_shortfall': 0,
                'cur_month_1st_calc': 0,
                'total_shortfall_period_one_claim': 0,
                'cur_month_total_shortfall': 0,
                'individual_shortfall_period_one_claim': 0,
                'cur_month_individual_shortfall': 0,
            } for _ in range(count)
        ]

    def start_simulation(self, target_dir=RESULT_DIR):
        s_time = time.time()
        target_dir = os.path.join(target_dir, datetime.now().strftime('%m_%d_%Y__%H_%M_%S'))
        os.makedirs(target_dir, exist_ok=True)

        logger.debug(f"Total members in the group: {self._total}")

        # ============================== Subgroup Setup ========================================
        step1_ev1 = self._total
        step2 = self._total / 5
        step3 = round(step2 / 2.3333)
        step4 = step3 * 5
        step5 = step1_ev1 - step4
        step6 = step5 / 6
        step7 = round(step6 / 2)
        step8 = step7 * 6
        step9 = step5 - step8
        step10 = step9 / 7
        step11 = int(step10 / 2)
        step12 = step11 * 7
        step13 = step9 - step12
        step14 = int(step13 / 4)
        step15 = step13 % 4
        if step15 == 1:
            step3 -= 1
            step7 += 1
        elif step15 == 2:
            step3 -= 1
            step11 += 1
        elif step15 == 3:
            step3 -= 1
            step14 += 2

        # Assigning number to the group, condition checking for group == 4
        group_num = 1
        group_mem_count = 0
        temp_val_four = step14 * 4
        offset = 0
        for i in range(temp_val_four):
            self._u_d[i + offset]['orig_sbg_num'] = group_num
            self._u_d[i + offset]['remaining_orig_sbg'] = 4
            self._u_d[i + offset]['cur_sbg_num'] = group_num
            self._u_d[i + offset]['members_cur_sbg'] = 4
            group_mem_count += 1
            if group_mem_count == 4:
                group_num += 1
                group_mem_count = 0
        offset += temp_val_four

        # condition checking for group == 5
        temp_val_five = step3 * 5
        for i in range(temp_val_five):
            self._u_d[i + offset]['orig_sbg_num'] = group_num
            self._u_d[i + offset]['remaining_orig_sbg'] = 5
            self._u_d[i + offset]['cur_sbg_num'] = group_num
            self._u_d[i + offset]['members_cur_sbg'] = 5
            group_mem_count += 1
            if group_mem_count == 5:
                group_num += 1
                group_mem_count = 0
        offset += temp_val_five

        # condition checking for group == 6
        temp_val_six = step7 * 6
        for i in range(temp_val_six):
            self._u_d[i + offset]['orig_sbg_num'] = group_num
            self._u_d[i + offset]['remaining_orig_sbg'] = 6
            self._u_d[i + offset]['cur_sbg_num'] = group_num
            self._u_d[i + offset]['members_cur_sbg'] = 6
            group_mem_count += 1
            if group_mem_count == 6:
                group_num += 1
                group_mem_count = 0
        offset += temp_val_six

        # condition checking for group == 7
        temp_val_seven = step11 * 7
        for i in range(temp_val_seven):
            self._u_d[i + offset]['orig_sbg_num'] = group_num
            self._u_d[i + offset]['remaining_orig_sbg'] = 7
            self._u_d[i + offset]['cur_sbg_num'] = group_num
            self._u_d[i + offset]['members_cur_sbg'] = 7
            group_mem_count += 1
            if group_mem_count == 7:
                group_num += 1
                group_mem_count = 0

        checksum = offset + temp_val_seven
        if checksum != self._total:
            raise ValueError(f"Initial group checksum failed: checksum:{checksum} != EV1:{self._total}")
        logger.debug({"D": temp_val_four, "A": temp_val_five, "B": temp_val_six, "C": temp_val_seven})

        logger.debug(
            f'Group4 members: {step14}, Group5 members: {step3}, Group6 members: {step7}, '
            f'Group7 members: {step11}, Total group: {step14 * 4 + step3 * 5 + step7 * 6 + step11 * 7}')

        # ========================================= Role Assignment =========================================
        # ROLE 1
        role_honest_defectors = int(self._total * self.ev['perc_honest_defectors'])
        defectors = random.sample(range(self._total), role_honest_defectors)
        non_defectors = [i for i in range(self._total) if i not in defectors]
        role_low_morale = int(self._total * self.ev['perc_low_morale'])
        low_morales = random.sample(non_defectors, role_low_morale)
        for i in range(self._total):
            self._u_d[i]['pri_role'] = \
                'defector' if i in defectors else 'low-morale' if i in low_morales else 'unity-role'

        # ROLE 2
        # temp_val_four users and pick remaining users randomly to be equal with EV6
        # (percentage of members who are unwilling to act alone)
        remaining = int(self.ev['perc_independent'] * self._total) - temp_val_four
        rand_dep_user = random.sample(range(temp_val_four, self._total), remaining) if remaining > 0 else []
        for i in range(self._total):
            self._u_d[i]['sec_role'] = 'dependent' if (i < temp_val_four or i in rand_dep_user) else 'independent'

        # ========================================= Period =========================================
        for self.period in range(self.count):
            if self.period > 0:
                self._s_d[self.period] = copy.deepcopy(self._s_d[self.period - 1])
            # RsA
            cur_month_1st_calc = self.cov_req / self._s_d[self.period]['valid_remaining']
            self._s_d[self.period]['cur_month_1st_calc'] = cur_month_1st_calc
            for i in range(self._total):
                # Current Months First Premium Calculation
                self._u_d[i]['cur_month_1st_calc'] = cur_month_1st_calc
                self._u_d[i]['credit_to_savings_account'] = self.cov_req / self._total
                if self.period == 0:
                    self._u_d[i]['cur_month_sec_cals'][0] = cur_month_1st_calc
                else:
                    wallet_balance = \
                        cur_month_1st_calc + int(self._u_d[i]['debit_to_savings_account'][self.period - 1]) - \
                        self._u_d[i]['wallet_no_claim_refund'] - self._u_d[i]['wallet_reorg_refund'] - \
                        self._u_d[i]['wallet_claim_award']
                    self._u_d[i]['wallet_balance'] = wallet_balance
                    self._u_d[i]['cur_month_sec_cals'][self.period] = wallet_balance

                self._u_d[i]['total_value_refunds'][self.period] = \
                    self._u_d[i]['wallet_no_claim_refund'] + self._u_d[i]['wallet_reorg_refund'] + \
                    self._u_d[i]['wallet_claim_award']

            if self.period == 0:       # Period 1
                self.user_func_1()
            else:
                self.user_func_2()

            # RsB
            for i in range(self.count):
                self._u_d[i]['cur_month_balance'] += self._u_d[i]['cur_month_1st_calc']
                if self.period > 0:
                    self._u_d[i]['debit_to_savings_account'][self.period] = 0

            self.sys_func_4()

            self.user_func_6()

            # RsC
            sd = self._s_d[self.period]
            self._s_d[self.period]['total_shortfall_period_one_claim'] = \
                sum([sd[k] for k in {'defection_shortfall', 'skip_shortfall', 'invalid_shortfall'}])
            self._s_d[self.period]['individual_shortfall_period_one_claim'] = \
                self._s_d[self.period]['total_shortfall_period_one_claim'] / sd['valid_remaining']
            self._s_d[self.period]['cur_month_total_shortfall'] = \
                sd['skip_shortfall'] + sd['invalid_shortfall'] / sd['valid_remaining']
            self._s_d[self.period]['cur_month_individual_shortfall'] = \
                self._s_d[self.period]['cur_month_total_shortfall'] / sd['valid_remaining']

            for i in range(self.count):
                self._u_d[i]['debit_to_savings_account'][self.period] += \
                    self._s_d[self.period]['individual_shortfall_period_one_claim']
                if self._u_d[i]['debit_to_savings_account'][self.period] > self._u_d[i]['credit_to_savings_account']:
                    msg = f"Period: {self.period}, User{i}: Debit(" \
                          f"{self._u_d[i]['debit_to_savings_account'][self.period]}) > Credit(" \
                          f"{self._u_d[i]['credit_to_savings_account']})"
                    raise ValueError(msg)

                self._u_d[i]['cur_month_balance'] += self._s_d[self.period]['cur_month_individual_shortfall']

            cmb = sum([u['cur_month_balance'] for u in self._u_d])
            if cmb != self.cov_req:
                raise ValueError(f"Invalid month balance - {cmb}, CV: {self.cov_req}")

            self.sys_func_8()

            self.sys_func_7()

            # ___SyFunc11___  (Reorg Stage 7)
            total = self.sy_rec_r[3].value + self.sy_rec_r[5].value + self.sy_rec_r[7].value
            if self.period != self.count - 1 and total > 0:
                # copy values of previous to current
                sy_rec_new_p = [self.sh_system.cell(2, k + 1) for k in range(23)]
                for k in range(1, 21):
                    sy_rec_new_p[k] = self.sh_system.cell(self.period * 3 + 2, k + 2)
                    sy_rec_new_p[k].value = self.sy_rec_r[k].value

                # Overwriting values in new row
                sy_rec_new_p[18].value = sy_rec_new_p[17].value
                for k in {3, 5, 6, 9, 11, 13, 14, 15, 17}:
                    sy_rec_new_p[k].value = 0

                self._checksum(11)
                self._checksum_sr1(sy_rec_new_p[1].value, 11)
            else:
                self.save_to_excel('user')
                self.save_to_excel('system')
                logger.info(f'Complete at period {self.period}, elapsed: {time.time() - s_time}')
                percent = round(self.sh_system.cell(3, 5).value / self._total * 100, 2)
                inc_premium = round((self.sy_rec_f[19].value / self.sh_system.cell(2, 21).value) * 100, 2)
                result_file = os.path.join(target_dir, "result.txt")
                results = [
                    self._total,
                    self.sy_rec_r[1].value,
                    round(((self._total - self.sy_rec_r[1].value) / self._total) * 100, 2),
                    round(self.sh_system.cell(2, 21).value),
                    int(self.sy_rec_f[19].value),
                    inc_premium,
                    self.sh_system.cell(3, 5).value,
                    self.ev[3] * 100,
                    percent,
                    self.pv[4] * 100
                ]
                lines = [
                    f'{results[0]} is the number of members at the start of the simulation\n',
                    f'{results[1]} is the number of valid members remaining at the end '
                    f'of the simulation\n',
                    f'{results[2]}% of '
                    f'policyholders left the group by end of simulation\n',
                    f'{results[3]} was the initial premium members were '
                    f'asked to pay.\n',
                    f'{results[4]} is the final premium members were asked to pay.\n',
                    f'Premiums increased by {results[5]}% by end of simulation\n',
                    f'self.SyRec 3 (period 0 finalize) = {results[6]}\n',
                    f'{results[7]}% of policyholders who were assigned to defect\n',
                    f'{results[8]}% of policyholders who actually defected\n',
                    f'{results[9]}% was the initial collapse threshold set for PV 5\n'
                ]
                logger.info('\n' + ''.join(lines))
                if not self.matrix:
                    with open(result_file, 'w') as f:
                        f.writelines(lines)
                else:
                    shutil.rmtree(target_dir, ignore_errors=True)
                return results

    def user_func_1(self):
        """
        User defection function
        """
        for i in range(self._total):
            if self._u_d[i]['pri_role'] == 'defector':
                defector_cnt = len([
                    u for u in self._u_d
                    if u['pri_role'] == 'defector' and u['cur_sbg_num'] == self._u_d[i]['cur_sbg_num']])
                self._u_d[i]['defector_cnt'] = defector_cnt
                if self._u_d[i]['sec_role'] == 'independent' or defector_cnt >= self.ev['dependent_thres']:
                    self._s_d[self.period]['valid_remaining'] -= 1
                    self._s_d[self.period]['defected_cnt'] += 1
                    self._s_d[self.period]['skipped_cnt'] += 1
                    self._poison_a_user(i)
                else:
                    self._u_d[i]['pri_role'] = 'low-morale'
        s_d = self._s_d[self.period]
        self._s_d[self.period]['defection_shortfall'] = s_d['defected_cnt'] * s_d['cur_month_1st_calc']
        self._s_d[self.period]['skip_shortfall'] = s_d['skipped_cnt'] * s_d['cur_month_1st_calc']

    def user_func_2(self):
        """"
        Pay Stage 2,  Pricing function
        """
        slope = (self.pv['ph_leave_ceiling'] - self.pv['ph_leave_floor']) / \
                (self.pv['prem_inc_ceiling'] - self.pv['prem_inc_floor'])

        for i in range(self._total):
            if self._u_d[i]['total_value_refunds'][self.period] == 0:
                matches = [p for p in range(self.period - 1, -1, -1) if self._u_d[i]['total_value_refunds'][p] == 0]
            else:
                matches = [p for p in range(self.period - 1, -1, -1) if self._u_d[i]['total_value_refunds'][p] != 0]
            mp = matches[-1] if matches else 0
            one_month_increase_perc = \
                int(self._u_d[i]['cur_month_sec_cals'][self.period]) / int(self._u_d[i]['cur_month_sec_cals'][mp]) - 1
            if one_month_increase_perc >= self.pv['prem_inc_floor']:
                ph_skip_perc = slope * (one_month_increase_perc - self.pv['prem_inc_floor']) + \
                               self.pv['ph_leave_floor']
                if random.uniform(0, 1) < ph_skip_perc:
                    self._poison_a_user(i)
                    break
            cum_inc_perc = \
                int(self._u_d[i]['cur_month_sec_cals'][self.period]) / self.cov_req * self.ev['total_member_cnt'] - 1
            if cum_inc_perc > self.pv['prem_inc_cum']:
                if random.uniform(0, 1) < self.pv['ph_leave_cum']:
                    self._poison_a_user(i)

    def _poison_a_user(self, index):
        for j in range(self._total):
            if self._u_d[j]['cur_sbg_num'] == self._u_d[index]['cur_sbg_num']:
                self._u_d[j]['members_cur_sbg'] -= 1
            if self._u_d[j]['orig_sbg_num'] == self._u_d[index]['orig_sbg_num']:
                self._u_d[j]['remaining_orig_sbg'] -= 1
        self._u_d[index]['cur_sbg_num'] = 0
        self._u_d[index]['members_cur_sbg'] = 0
        self._u_d[index]['sbg_status'] = 'NR'
        self._u_d[index]['cur_status'] = 'NR'
        self._u_d[index]['payable'] = 'NR'

    def sys_func_4(self):
        """"
        Invalidate subgroup function
        """
        for i in range(self._total):
            if self._u_d[i]['members_cur_sbg'] in {1, 2, 3} and self._u_d[i]['cur_status'] == 'paid':
                self._u_d[i]['sbg_status'] = 'invalid'
                self._u_d[i]['cur_status'] = 'paid-invalid'
                self._s_d[self.period]['invalid_cnt'] += 1
                self._s_d[self.period]['valid_remaining'] -= 1
                self._u_d[i]['wallet_reorg_refund'] = self._u_d[i]['cur_month_1st_calc']
                self._u_d[i]['cur_month_1st_calc'] = 0
        sd = self._s_d[self.period]
        self._s_d[self.period]['invalid_shortfall'] = sd['invalid_cnt'] * sd['cur_month_1st_calc']

    def user_func_6(self):
        """
        User Quit Function
        :return:
        """
        quit_list = []
        for i in range(self._total):
            if self._u_d[i]['cur_status'] == 'paid-invalid':
                if self._u_d[i]['pri_role'] == 'low-morale':
                    if random.uniform(0, 1) > self.ev['low_morale_quit_prob']:
                        for j in range(self._total):
                            if self._u_d[j]['cur_sbg_num'] == self._u_d[i]['cur_sbg_num']:
                                self._u_d[j]['sbg_reorg_cnt'] += 1
                        if self._u_d[i]['sec_role'] == 'dependent':
                            quit_list.append(i)
                    else:
                        self._poison_a_user(i)
                        self._s_d[self.period]['quit_cnt'] += 1
                elif self._u_d[i]['pri_role'] == 'unity':
                    for j in range(self._total):
                        if self._u_d[j]['cur_sbg_num'] == self._u_d[i]['cur_sbg_num']:
                            self._u_d[j]['sbg_reorg_cnt'] += 1
        for i in quit_list:
            if self._u_d[i]['sbg_reorg_cnt'] < 2:
                self._poison_a_user(i)
                self._s_d[self.period]['quit_cnt'] += 1

    def sys_func_7(self):
        """"
        Reorganization of Users
        """
        invalid_users = [i for i in range(self._total) if self.get_cur_status(i) == 'paid-invalid']
        for path in {1, 2}:
            path_users = [i for i in invalid_users if self.get_remaining_num_cur_subgroup(i) == path]
            # First Attempt
            invalid_list = list(set([self.get_cur_subgroup(i) for i in path_users]))
            valid_list = list(set(
                [self.get_cur_subgroup(i) for i in range(self._total)
                 if self.get_subgroup_status(i) == 'valid' and self.get_remaining_num_cur_subgroup(i) == (7 - path)]))
            while True:
                # Assignment First Attempt
                if invalid_list and valid_list:
                    need_match = invalid_list[0]
                    give_match = random.sample(valid_list, 1)[0]
                    for i in path_users[:]:
                        if self.get_cur_subgroup(i) == need_match:
                            self.set_cur_subgroup(i, give_match)
                            self.set_remaining_num_cur_subgroup(i, 7)
                            self.set_subgroup_status(i, 'valid')
                            self.set_cur_status(i, 'reorg')
                            self.set_reorg_time(i, self.get_reorg_time(i) + 1)
                            path_users.remove(i)
                    invalid_list.remove(need_match)
                    for i in range(self._total):
                        if self.get_cur_subgroup(i) == give_match:
                            self.set_remaining_num_cur_subgroup(i, 7)
                    valid_list.remove(give_match)
                if not invalid_list:
                    if path_users:
                        logger.warning(f"Period {self.period}, SysFunc7: Path{path} invalid is empty "
                                       f"but run set is not empty in the 1st attempt!")
                    break
                elif not valid_list:      # Second attempt
                    filtered_list = list(set(
                        [self.get_cur_subgroup(i) for i in range(self._total)
                         if self.get_subgroup_status(i) == 'valid' and
                            self.get_remaining_num_cur_subgroup(i) == (6 - path)]))
                    while filtered_list:
                        need_match = invalid_list[0]
                        give_match = random.sample(filtered_list, 1)[0]
                        for i in path_users[:]:
                            if self.get_cur_subgroup(i) == need_match:
                                self.set_cur_subgroup(i, give_match)
                                self.set_remaining_num_cur_subgroup(i, 6)
                                self.set_subgroup_status(i, 'valid')
                                self.set_cur_status(i, 'reorg')
                                self.set_reorg_time(i, self.get_reorg_time(i) + 1)
                                path_users.remove(i)
                        invalid_list.remove(need_match)
                        for i in range(self._total):
                            if self.get_cur_subgroup(i) == give_match:
                                self.set_remaining_num_cur_subgroup(i, 6)
                        filtered_list.remove(give_match)
                        if not invalid_list:
                            if path_users:
                                logger.warning(f"Period {self.period}, SysFunc7: Path{path} invalid is empty "
                                               f"but run set is not empty in the 2nd attempt!")
                            break
                    break

        # Path 3
        path_3_users = [i for i in invalid_users if self.get_remaining_num_cur_subgroup(i) == 3]
        invalid_list = list(set([self.get_cur_subgroup(i) for i in path_3_users]))
        while len(invalid_list) >= 2:      # Path 3 Assignment first attempt
            need_match = invalid_list[0]
            give_match = invalid_list[1]
            for i in path_3_users:
                if self.get_cur_subgroup == need_match:
                    self.set_cur_subgroup(i, give_match)
                    self.set_remaining_num_cur_subgroup(i, 6)
                    self.set_subgroup_status(i, 'valid')
                    self.set_cur_status(i, 'reorg')
                    self.set_reorg_time(i, self.get_reorg_time(i) + 1)
            invalid_list.remove(need_match)
            for i in range(self._total):
                if self.get_cur_subgroup(i) == give_match and i not in path_3_users:
                    self.set_remaining_num_cur_subgroup(i, 6)
                    self.set_subgroup_status(i, 'valid')
                    self.set_cur_status(i, 'reorg')
                    self.set_reorg_time(i, self.get_reorg_time(i) + 1)
            invalid_list.remove(give_match)
            path_3_users = [i for i in path_3_users if self.get_cur_subgroup(i) not in {need_match, give_match}]
            if not invalid_list:
                if not path_3_users:
                    return
        # Path 3 Second Attempt
        valid_list = list(set(
            [self.get_cur_subgroup(i) for i in range(self._total)
             if self.get_subgroup_status(i) == 'valid' and self.get_remaining_num_cur_subgroup(i) == 4]))
        # TODO: If invalid_list is empty and valid_list is not empty?
        if invalid_list and valid_list:
            need_match = invalid_list[0]
            give_match = random.sample(valid_list, 1)[0]
            for i in path_3_users[:]:
                if self.get_cur_subgroup(i) == need_match:
                    self.set_cur_subgroup(i, give_match)
                    self.set_remaining_num_cur_subgroup(i, 7)
                    self.set_subgroup_status(i, 'valid')
                    self.set_cur_status(i, 'reorg')
                    self.set_reorg_time(i, self.get_reorg_time(i) + 1)
                    path_3_users.remove(i)
            for i in range(self._total):
                if self.get_cur_subgroup(i) == give_match:
                    self.set_remaining_num_cur_subgroup(i, 7)
            valid_list.remove(give_match)
            if path_3_users:
                logger.warning(f"Period {self.period}, SysFunc7: Path3 invalid is empty but "
                               f"run set is not empty in the 2nd attempt!")

    def sys_func_8(self):
        """"
        Determine Claims
        """
        x = random.uniform(0, 1)
        claimant = random.sample([i for i in range(self.count) if self._u_d[i]['sbg_status'] == 'valid'], 1)[0]
        for i in range(self.count):
            if self._u_d[i]['cur_status'] == 'paid':
                if x >= self.ev['chance_of_claim']:
                    self._u_d[i]['cur_month_premium'] = self._u_d[i]['cur_month_balance']
                else:   # Claim occurred
                    self._u_d[claimant]['wallet_claim_award'] += self._u_d[i]['cur_month_balance']
                    for m in range(self.bundling):
                        self._u_d[claimant]['wallet_claim_award'] += self._u_d[i]['prior_premiums'][m]
                        self._u_d[i]['prior_premiums'][m] = 0

                self._u_d[i]['cur_month_balance'] = 0


if __name__ == '__main__':

    _ev = {
        'total_member_cnt': 60,
        'monthly_premium': 0,
        'chance_of_claim': 25,
        'perc_honest_defectors': 0.3,
        'perc_low_morale': 0.2,
        'perc_independent': 20,
        'dependent_thres': 2,
        'low_morale_quit_prob': .3333,
    }
    _pv = {
        'prem_inc_floor': 30,
        'ph_leave_floor': 20,
        'prem_inc_ceiling': 50,
        'ph_leave_ceiling': 25,
        'prem_inc_cum': 30,
        'ph_leave_cum': 20,
    }
    tps = TandaPaySimulatorV2(ev=_ev, pv=_pv)
    tps.start_simulation()
