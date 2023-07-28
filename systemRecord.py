


class SystemRecord:
    valid_remaining = 0                         # SysRec1: Valid members remaining (init to EV1)
    defected_cnt = 0                            # SysRec3: Number of defected members (init to 0)
    skipped_cnt = 0                             # SysRec5: number of members skipped (init to 0)
    invalid_cnt = 0                             # SysRec6: Number of invalid members (init to 0)
    reorged_cnt = 0                             # SysRec8: number of members that have reorged (init to 0) 
    quid_cnt = 0                                # SysRec7: Number of members that quit (init to 0) 
   

    defection_shortfall = 0                     # SysRec9: Fracture debt from defections (init to 0)
    invalid_shortfall = 0                       # SysRec12: Fracture debt from invalid new (init to 0)
    skip_shortfall = 0                          # SysRec10: Fracture debt from skips new (init to 0)
    
    individual_shortfall_period_one_claim = 0  
    total_shortfall_period_one_claim = 0        # Fracture Debt total (init to 0)
    cur_moonth_individual_shortfall = 0
    cur_month_total_shortfall = 0


