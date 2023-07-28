
class SystemRecord:
    def __init__(self, total_member_cnt):
        self.valid_remaining = total_member_cnt          # SysRec1:  Number of valid remembers remaining (init to EV1 a.k.a total_member_cnt)
        self.defected_cnt = 0                            # SysRec3:  Number of defected members (init to 0)
        self.skipped_cnt = 0                             # SysRec5:  Number of members skipped (init to 0)
        self.invalid_cnt = 0                             # SysRec6:  Number of invalid members (init to 0)
        self.reorged_cnt = 0                             # SysRec8:  Number of members that have reorged (init to 0) 
        self.quid_cnt = 0                                # SysRec7:  Number of members that quit (init to 0) 

        self.defection_shortfall = 0                     # SysRec9:  Fracture debt from defections (init to 0)
        self.invalid_shortfall = 0                       # SysRec12: Fracture debt from invalid new (init to 0)
        self.skip_shortfall = 0                          # SysRec10: Fracture debt from skips new (init to 0)
        
        self.individual_shortfall_period_one_claim = 0  
        self.total_shortfall_period_one_claim = 0        # Fracture Debt total (init to 0)
        self.cur_moonth_individual_shortfall = 0
        self.cur_month_total_shortfall = 0
        self.claimed = False
