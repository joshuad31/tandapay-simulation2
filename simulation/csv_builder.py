import copy
import csv
import os

class CSV_Builder:
    """
    This class contains operations for generating .csv files for the simulation's debug run functionality
    """

    def __init__(self, sys_csv_file='system_record.csv', user_csv_file='user_record.csv'):
        """
        Initializes csv files for system record and user record

        :param sys_csv_file: path to csv where you will store system record
        :param user_csv_file: path to csv where you will store user records
        """
        self.sys_csv_file = sys_csv_file
        self.user_csv_file = user_csv_file
        # Initialize System Record CSV
        with open(self.sys_csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Period', 'Valid_Remaining', 'Defected_Cnt', 'Skipped_Cnt', 'Invalid_Cnt', 
                             'Reorged_Cnt', 'Quit_Cnt', 'Defection_Shortfall', 'Invalid_Shortfall', 
                             'Skip_Shortfall', 'Shortfall_Debt_Individual', 'Shortfall_Debt_Total',
                             'Shortfall_Credit_Individual', 'Shortfall_Credit_Total', 'First_Premium_Calc', 'Claimed'])

        # Initialize User Record CSV
        with open(self.user_csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Period', 'Orig_Sbg_Num', 'Remaining_Orig_Sbg', 'Cur_Sbg_Num', 'Members_Cur_Sbg',
                             'Sbg_Status', 'Pri_Role', 'Sec_Role', 'Cur_Status', 'Reorged_Cnt', 'Payable', 
                             'Defector_Cnt', 'Wallet_Balance', 'Wallet_Claim_Award', 'Claim_Refund', 'Invalid_Refund',
                             'Premium_Balance', 'Cur_Month_Premium', 'Credit_To_Savings_Account', 'Sbg_Reorg_Cnt', 
                             'Second_Premium_Calc', 'Total_Value_Refund', 'Debt_To_Savings_Account'])

    def record(self, period, env_vars, sys_rec, pricing_vars, user_list):
        """
        passed as a function pointer to simulation so that we can record
        between periods. saves data to the CSVs

        :param period: current period the simulation is on
        :param env_vars: environment variables we are running the simulation with
        :param sys_rec: system record we are initializing the simulation with
        :param pricing_vars: pricing variables we are running the simulation with
        :param user_list: list of user_record objects which represents the users
        """

        # Record System_Record
        with open(self.sys_csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([period, sys_rec.valid_remaining, sys_rec.defected_cnt, sys_rec.skipped_cnt,
                             sys_rec.invalid_cnt, sys_rec.reorged_cnt, sys_rec.quit_cnt, sys_rec.defection_shortfall,
                             sys_rec.invalid_shortfall, sys_rec.skip_shortfall, sys_rec.shortfall_debt_individual,
                             sys_rec.shortfall_debt_total, sys_rec.shortfall_credit_individual, sys_rec.shortfall_credit_total,
                             sys_rec.first_premium_calc, sys_rec.claimed])

        # Record User_Record(s)
        with open(self.user_csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for user in user_list:
                writer.writerow([period, user.orig_sbg_num, user.remaining_orig_sbg, user.cur_sbg_num, user.members_cur_sbg,
                                 user.sbg_status, user.pri_role, user.sec_role, user.cur_status, user.reorged_cnt, 
                                 user.payable, user.defector_cnt, user.wallet_balance, user.wallet_claim_award, 
                                 user.claim_refund, user.invalid_refund, user.premium_balance, user.cur_month_premium, 
                                 user._credit_to_savings_account, user.sbg_reorg_cnt, user.second_premium_calc_list[period], 
                                 user.total_value_refund_list[period], user.debt_to_savings_account_list[period]])
    
    # returns a tuple containing the absolute path of sys_csv and user_csv
    def get_absolute_paths(self):
        """
        gets absolute paths of system and user record

        :return: Tuple containing (sys_csv_path, user_csv_path)
        """

        sys_csv_absolute_path = os.path.abspath(self.sys_csv_file)
        user_csv_absolute_path = os.path.abspath(self.user_csv_file)
        return (sys_csv_absolute_path, user_csv_absolute_path)
