# Requirements

1. Requires you to have Python 3 installed.
2. If on windows, we recommend installing Python via the Microsoft store, or with `winget` package manager.
3. numpy, scipy, and PySide2 python packages
4. Git (optional. used to clone repo during installation. You can also just download the source directly from the Github page

# Installation

## Linux, MacOS

1. Go to a terminal and enter the command `git clone https://github.com/KevinCPP/tandapay-simulation2`. Navigate to the project directory `cd tandapay-simulation2`
2. Install the dependencies listed in dependencies.txt. This can be done by entering the command `pip install -r dependencies.txt`
3. simply execute the main file using the command `python3 main.py`

## Windows

1. Run Windows Powershell and enter the command `git clone https://github.com/KevinCPP`. If you don't have git, try `winget install Git` or install the Git CLI tool from their website.
2. Install the dependencies listed in dependencies.txt. This can be done by entering the command `pip install -r dependencies.txt`. You will need to have python installed before doing this, which can be gotten with `winget install python3`. If you already have python installed, try uninstalling it and reinstalling it via winget or the Microsoft Store GUI.
3. simply execute the main file using the command `python main.py`

# Usage

## Background

The TandaPay simulation is supposed to model the behavior of users of the Tandapay decentralized insurance/whistleblower protocol. The chief goal of the simulation is to study the relationship between the number of users who defect (disagree with a claim when it happens, and refuse to pay, causing remaining members' premiums to increase) and group collapse.

We wanted to find what percentage of honest defectors are required to cause groups to collapse, in order to find out if the protocol serves it's purpose of being resilient to collusion to take advantage of it.

The simulation can result in either a Win, Loss, or Draw, with probability depending on the initial variables the simulation is executed with.

## Basic Simulation Runs

These can help you get a quick, rough idea of the simulation's output for a single set of variables. Simply click "Run Simulation" and the simulation will be executed using the values you specified in the "Settings" menu. You can alter the "Sample Size" variable to alter the number of runs, this getting a more representative percentage of wins/losses/draws. Results are stored in "History"

## Statistics Runs

Statistics can help you get a deeper understanding of how the simulation behaves with a specific set of variables. It calculates some additional things such as mean, standard deviation, confidence intervals, and hypothesis tests.

It uses the "alpha" value provided in settings for all confidence intervals and hypothesis tests. This means if alpha is 0.05, it will yield 95% confidence intervals and allow for a 5% chance of being incorrect for hypothesis tests.

Statistics runs the simulation for n="Trial Sample Size" * k="Trial Count" for a total of `n * k` simulation runs. It uses the Central Limit Theorem to create a probability distribution of the amount of wins, losses, and draws based on these runs.

"Test Type" specifies the type of hypothesis test you want to do, "Outcome To Test" specifies the outcome you want to test (win, loss, draw, ...), and "Value  to test" is which value you want to test it against. So, if "Test Type" is "greater", "Outcome to Test" is "num_wins", and "value to test" is 0.50, we're going to run a hypothesis test that answers the question, "Can we say with `(alpha * 100)%` chance of being incorrect that num_wins > 50%?"

Results of statistics are also stored in history

## Searching Runs

Searching is a method for studying the relationships between initial variables and simulation outcomes. It does this by generating Regression models after doing multiple simulation runs with different values for the variable you're trying to study, which models the relationship between simulation outcomes and the value of the variable you are studying.

"Target Percent" and "Outcome to Target" specify what percentage you're trying to solve for with the linear regression algorithm, and whether you're studying wins/losses/draws, respectively.

"Min value" and "Max value" specify the range of values you want to investigate for this searching run. If just left to defaults (recommended), searching will search the entire domain for the variable you're investigating.

"Steps" is the number of steps between the minimum and maximum values for the variable you're studying. For example, if you set "Steps" to 20, there will be 20 points of data that the regression model is built upon. Beware setting steps too high, as setting it too high can introduce variability into your results and make your regression model less accurate, by amplifying noise from variability. The default of 20 is good in most cases.

"Order" is what order Regression model you want to use. For example, if "Order"=3, it will use a model of the form `x -> ax^3 + bx^2 + cx + d` to model the relationship between the variable you're studying and the outcome you're targeting. Again, higher is not always better, as a higher Regression model can take noise into account and be less accurate. "Order"=3 seemed to be the sweet spot.

Searching finally finds the roots of the regression model to give you an idea for what value the attribute you're searching needs to be to reach the target percentage of the outcome you're targetting. Select which variable you want to investigate with "Attribute to search". Search results are also stored in "History"

## Run Debug

Will run the simulation once utilizing the settings specified in the Settings menu. Will generate two .csv files in the project's root directory; sys_rec.csv and user_rec.csv, which shows the system record and user record between each run of the simulation.

This is useful for getting an idea of how the simulation calculated it's outcome, as it  gives an extremely detailed account of the changes in most of the mutable internal simulation variables.

## Other Features

- Settings: Use this menu to change settings and initial values to run the simulation with
- History: Use this menu to see the history of your results, so you can easily reference them later. Stored in an SQLite database by default

# Documentation

Most functions have a docstring within the source code that explains what it does, the parameters it takes, and what it returns. the ones that don't are either self explanatory or are helper functions to others. Plaintext documentation generated by sphinx also included below.

# Modules

tandapay-simulation2
********************

* main module

  * "Main"

    * "Main.run_about_callback()"

    * "Main.run_debug_callback()"

    * "Main.run_history_callback()"

    * "Main.run_searching_callback()"

    * "Main.run_simulation_callback()"

    * "Main.run_statistics_callback()"

    * "Main.save_settings_callback()"

* simulation package

  * Submodules

  * simulation.csv_builder module

    * "CSV_Builder"

      * "CSV_Builder.get_absolute_paths()"

      * "CSV_Builder.record()"

  * simulation.environment_variables module

    * "Environment_Variables"

      * "Environment_Variables.calculate_member_variables()"

      * "Environment_Variables.chance_of_claim"

      * "Environment_Variables.cov_req"

      * "Environment_Variables.dependent_thres"

      * "Environment_Variables.get_limits()"

      * "Environment_Variables.low_morale_quit_prob"

      * "Environment_Variables.max_period"

      * "Environment_Variables.member_cnt_defectors"

      * "Environment_Variables.member_cnt_dependent"

      * "Environment_Variables.member_cnt_independent"

      * "Environment_Variables.member_cnt_low_morale"

      * "Environment_Variables.member_cnt_unity"

      * "Environment_Variables.monthly_premium"

      * "Environment_Variables.perc_honest_defectors"

      * "Environment_Variables.perc_independent"

      * "Environment_Variables.perc_low_morale"

      * "Environment_Variables.queueing"

      * "Environment_Variables.total_member_cnt"

  * simulation.other_variables module

    * "Other_Variables"

      * "Other_Variables.test_outcome"

      * "Other_Variables.test_type"

    * "OutcomeEnum"

      * "OutcomeEnum.DRAW"

      * "OutcomeEnum.LOSS"

      * "OutcomeEnum.WIN"

  * simulation.period_functions module

    * "rsa_calculate_premiums()"

    * "rsb_payback_debt()"

    * "rsc_calculate_shortfall()"

  * simulation.pricing_variables module

    * "Pricing_Variables"

      * "Pricing_Variables.get_limits()"

  * simulation.queueing module

    * "queueing_function()"

  * simulation.remove_user module

    * "evaluate_probability()"

    * "is_approx_equal()"

    * "remove_user()"

  * simulation.results_aggregator module

    * "Results_Aggregator"

      * "Results_Aggregator.add_result()"

      * "Results_Aggregator.add_to_draw_totals()"

      * "Results_Aggregator.add_to_loss_totals()"

      * "Results_Aggregator.add_to_win_totals()"

      * "Results_Aggregator.calculate_averages()"

      * "Results_Aggregator.calculate_maximums()"

      * "Results_Aggregator.calculate_minimums()"

      * "Results_Aggregator.calculate_secondaries()"

      * "Results_Aggregator.get_string()"

  * simulation.role_assignment module

    * "role_assignment()"

    * "test_role_assignment()"

  * simulation.sf4_invalidate_subgroups module

    * "sf4_invalidate_subgroups()"

  * simulation.sf7_reorganization_of_users module

    * "combine_groups()"

    * "combine_size()"

    * "group_data"

    * "sf7_reorganization_of_users()"

    * "test_combine_size()"

  * simulation.sf8_determine_claims module

    * "sf8_determine_claims()"

  * simulation.simulation module

    * "base_simulation()"

    * "exec_simulation()"

    * "exec_simulation_debug()"

    * "exec_simulation_multiple()"

    * "take_snapshot()"

  * simulation.simulation_results module

    * "ResultsEnum"

      * "ResultsEnum.DRAW_A"

      * "ResultsEnum.DRAW_B"

      * "ResultsEnum.LOSS_A"

      * "ResultsEnum.LOSS_B"

      * "ResultsEnum.WIN_A"

      * "ResultsEnum.WIN_B"

      * "ResultsEnum.get_result_str()"

    * "Simulation_Results"

  * simulation.subgroup_setup module

    * "subgroup_setup()"

    * "test_subgroup_setup()"

    * "test_subgroup_setup_basic_print()"

  * simulation.system_record module

    * "System_Record"

      * "System_Record.calculate_vars()"

      * "System_Record.claimed"

      * "System_Record.defected_cnt"

      * "System_Record.defection_shortfall"

      * "System_Record.first_premium_calc"

      * "System_Record.invalid_cnt"

      * "System_Record.invalid_shortfall"

      * "System_Record.quit_cnt"

      * "System_Record.reorged_cnt"

      * "System_Record.shortfall_credit_individual"

      * "System_Record.shortfall_credit_total"

      * "System_Record.shortfall_debt_individual"

      * "System_Record.shortfall_debt_total"

      * "System_Record.skip_shortfall"

      * "System_Record.skipped_cnt"

      * "System_Record.valid_remaining"

  * simulation.uf1_determine_defectors module

    * "test_uf1_determine_defectors()"

    * "uf1_determine_defectors()"

  * simulation.uf2_pricing_function module

    * "evaluate_cumulative()"

    * "evaluate_noref()"

    * "evaluate_qualifying()"

    * "evaluate_refund()"

    * "find_previous_matching_refund()"

    * "uf2_pricing_function()"

  * simulation.uf6_user_quit_function module

    * "increment_other_group_member_sbg_reorg_cnt()"

    * "uf6_user_quit_function()"

  * simulation.user_record module

    * "CurrentStatusEnum"

      * "CurrentStatusEnum.DEFECTED"

      * "CurrentStatusEnum.NR"

      * "CurrentStatusEnum.PAID"

      * "CurrentStatusEnum.PAID_INVALID"

      * "CurrentStatusEnum.QUIT"

      * "CurrentStatusEnum.REORG"

      * "CurrentStatusEnum.SKIPPED"

    * "PayableEnum"

      * "PayableEnum.NO"

      * "PayableEnum.NR"

      * "PayableEnum.YES"

    * "PrimaryRoleEnum"

      * "PrimaryRoleEnum.DEFECTOR"

      * "PrimaryRoleEnum.LOW_MORALE"

      * "PrimaryRoleEnum.UNITY"

    * "SecondaryRoleEnum"

      * "SecondaryRoleEnum.DEPENDENT"

      * "SecondaryRoleEnum.INDEPENDENT"

    * "User_Record"

      * "User_Record.credit_to_savings_account"

    * "ValidityEnum"

      * "ValidityEnum.INVALID"

      * "ValidityEnum.NR"

      * "ValidityEnum.VALID"

  * Module contents

* statistics package

  * Submodules

  * statistics.confidence_interval module

    * "calculate_confidence_interval()"

  * statistics.hypothesis_test module

    * "TestTypeEnum"

      * "TestTypeEnum.GREATER"

      * "TestTypeEnum.LESS"

      * "TestTypeEnum.TWOTAILED"

    * "perform_hypothesis_test()"

  * statistics.searching module

    * "Result"

    * "Searching"

      * "Searching.basic_search()"

      * "Searching.get_linreg()"

      * "Searching.perform_full_search()"

  * statistics.searching_attributes module

  * statistics.statistics_aggregator module

    * "Statistics_Aggregator"

      * "Statistics_Aggregator.add_result()"

      * "Statistics_Aggregator.calculate_confidence_intervals()"

      * "Statistics_Aggregator.calculate_hypothesis_test()"

      * "Statistics_Aggregator.calculate_stats()"

      * "Statistics_Aggregator.get_string()"

      * "Statistics_Aggregator.print_dicts()"

  * statistics.statistics_attributes module

  * statistics.statistics_runner module

    * "Statistics_Runner"

      * "Statistics_Runner.get_string()"

      * "Statistics_Runner.run()"

  * Module contents

* ui package

  * Submodules

  * ui.ev_layout module

    * "EV_Layout"

      * "EV_Layout.get_env_vars()"

      * "EV_Layout.get_ev_layout()"

  * ui.history_menu module

    * "History_Menu"

      * "History_Menu.populate_results()"

      * "History_Menu.show_result()"

      * "History_Menu.staticMetaObject"

  * ui.initialize module

    * "initialize()"

  * ui.iv_layout module

    * "IV_Layout"

      * "IV_Layout.get_iv_layout()"

      * "IV_Layout.save()"

  * ui.main_menu module

    * "Main_Menu"

      * "Main_Menu.get_title_widget()"

      * "Main_Menu.history()"

      * "Main_Menu.quit()"

      * "Main_Menu.run_debug()"

      * "Main_Menu.run_searching()"

      * "Main_Menu.run_simulation()"

      * "Main_Menu.run_statistics()"

      * "Main_Menu.settings()"

      * "Main_Menu.staticMetaObject"

  * ui.old_main_menu module

  * ui.old_settings_menu module

    * "SettingsDialog"

      * "SettingsDialog.get_ok_cancel_buttons()"

      * "SettingsDialog.get_settings_dialog()"

      * "SettingsDialog.get_settings_widget()"

      * "SettingsDialog.get_two_column_layout()"

      * "SettingsDialog.save_and_close()"

  * ui.ov_layout module

    * "OV_Layout"

      * "OV_Layout.get_other_vars()"

      * "OV_Layout.get_ov_layout()"

  * ui.pv_layout module

    * "PV_Layout"

      * "PV_Layout.get_pricing_vars()"

      * "PV_Layout.get_pv_layout()"

  * ui.results_menu module

    * "Results_Window"

      * "Results_Window.set_results_text()"

      * "Results_Window.staticMetaObject"

  * ui.results_window module

    * "Results_Window"

      * "Results_Window.set_results_text()"

      * "Results_Window.staticMetaObject"

  * ui.searching_menu module

    * "Searching_Menu"

      * "Searching_Menu.create_menu_dialog()"

      * "Searching_Menu.open_searching_menu()"

      * "Searching_Menu.run()"

  * ui.settings_menu module

    * "Settings_Menu"

      * "Settings_Menu.get_ok_cancel_layout()"

      * "Settings_Menu.get_settings_layout()"

      * "Settings_Menu.open_settings_menu()"

      * "Settings_Menu.save_and_close()"

  * ui.statistics_settings_menu module

  * ui.stats_layout module

    * "Stats_Layout"

      * "Stats_Layout.get_stats_layout()"

      * "Stats_Layout.save()"

  * ui.ui_context module

    * "UI_Context"

  * ui.ui_element_factory module

    * "UI_Element_Factory"

      * "UI_Element_Factory.getValue()"

      * "UI_Element_Factory.make_dropdown_entry_element()"

      * "UI_Element_Factory.make_file_explorer_element()"

      * "UI_Element_Factory.make_float_entry_element()"

      * "UI_Element_Factory.make_numeric_entry_element()"

      * "UI_Element_Factory.make_push_button_element()"

      * "UI_Element_Factory.make_static_textbox_element()"

  * Module contents

* util package

  * Submodules

  * util.ini_handler module

    * "INI_Handler"

      * "INI_Handler.read_environment_variables()"

      * "INI_Handler.read_other_variables()"

      * "INI_Handler.read_pricing_variables()"

      * "INI_Handler.write_environment_variables()"

      * "INI_Handler.write_other_variables()"

      * "INI_Handler.write_pricing_variables()"

  * util.results_db module

    * "Results_DB"

      * "Results_DB.add_result()"

      * "Results_DB.create_table()"

      * "Results_DB.get_result_by_id()"

      * "Results_DB.get_results()"

      * "Results_DB.set_remote_db()"

  * Module contents

# Simulation Docs

simulation package
******************


Submodules
==========


simulation.csv_builder module
=============================

class simulation.csv_builder.CSV_Builder(sys_csv_file='system_record.csv', user_csv_file='user_record.csv')

   Bases: "object"

   This class contains operations for generating .csv files for the
   simulation's debug run functionality

   get_absolute_paths()

      gets absolute paths of system and user record

      Returns:
         Tuple containing (sys_csv_path, user_csv_path)

   record(period, env_vars, sys_rec, pricing_vars, user_list)

      passed as a function pointer to simulation so that we can record
      between periods. saves data to the CSVs

      Parameters:
         * **period** -- current period the simulation is on

         * **env_vars** -- environment variables we are running the
           simulation with

         * **sys_rec** -- system record we are initializing the
           simulation with

         * **pricing_vars** -- pricing variables we are running the
           simulation with

         * **user_list** -- list of user_record objects which
           represents the users


simulation.environment_variables module
=======================================

class simulation.environment_variables.Environment_Variables

   Bases: "object"

   This class encapsulates all of the environment variables.

   domain limited variables: - chance of claim: [25, 75] - percent
   honest defectors: [10, 45] - percent low morale: [10, 30] - percent
   independent: [20, 80] - dependent threshold: [2, 3] - queueing: [0,
   3]

   calculate_member_variables()

   property chance_of_claim

   property cov_req

   property dependent_thres

   get_limits(attribute: str)

   property low_morale_quit_prob

   property max_period

   property member_cnt_defectors

   property member_cnt_dependent

   property member_cnt_independent

   property member_cnt_low_morale

   property member_cnt_unity

   property monthly_premium

   property perc_honest_defectors

   property perc_independent

   property perc_low_morale

   property queueing

   property total_member_cnt


simulation.other_variables module
=================================

class simulation.other_variables.Other_Variables

   Bases: "object"

   Stores a collection of other variables that are used for simulation
   runs, but not in the actual simulation itself. Includes things like
   sample size, trial sample size, trial count, ...

   property test_outcome

   property test_type

class simulation.other_variables.OutcomeEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   Can be a win, loss, or draw

   DRAW = 2

   LOSS = 1

   WIN = 0


simulation.period_functions module
==================================

simulation.period_functions.rsa_calculate_premiums(env_vars, sys_rec, user_list, period)

   This function, RSA, calculates users' premiums

   Parameters:
      * **env_vars** -- Takes in simulation environment variables

      * **sys_rec** -- Takes in simulation system record for this
        period

      * **user_list** -- Takes in the list of users in this simulation
        run

      * **period** -- Takes in the current period the simulation is on

simulation.period_functions.rsb_payback_debt(env_vars, sys_rec, user_list, period)

   This function, RSB, pays back their debts

   Parameters:
      * **env_vars** -- Takes in simulation environment variables

      * **sys_rec** -- Takes in simulation system record for this
        period

      * **user_list** -- Takes in the list of users in this simulation
        run

      * **period** -- Takes in the current period the simulation is on

simulation.period_functions.rsc_calculate_shortfall(env_vars, sys_rec, user_list, period)

   This function, RSC, calculates shortfalls

   Parameters:
      * **env_vars** -- Takes in simulation environment variables

      * **sys_rec** -- Takes in simulation system record for this
        period

      * **user_list** -- Takes in the list of users in this simulation
        run

      * **period** -- Takes in the current period the simulation is on


simulation.pricing_variables module
===================================

class simulation.pricing_variables.Pricing_Variables

   Bases: "object"

   Encapsulates the pricing variables we are running the simulation
   with

   get_limits(attribute: str)


simulation.queueing module
==========================

simulation.queueing.queueing_function(user_list)

   Queueing delays the refunds that are given to the users.

   Parameters:
      **user_list** -- takes in the list of users for this simulation
      run


simulation.remove_user module
=============================

simulation.remove_user.evaluate_probability(prob) -> bool

   evaluates a probability between 0 and 1. For example, if 0.5 is
   passed, it will return true 50% of the time and false 50% of the
   time.

   Parameters:
      **prob** -- probability to evaluate

simulation.remove_user.is_approx_equal(a, b, epsilon)

   Tests for equality with a margin of error

   Parameters:
      * **a** -- floating point number 1

      * **b** -- floating point number 2

      * **epsilon** -- margin of error allowed

   Returns:
      >>|a - b|<< < epsilon

simulation.remove_user.remove_user(user_list, index, reason='No reason provided.')

   removes a user from the user list. This involves altering the
   subgroup information of other users who are effected.

   Parameters:
      * **user_list** -- takes in the list of users in this simulation
        run

      * **index** -- at what index user should be removed

      * **reason** -- reason user was removed (optional)


simulation.results_aggregator module
====================================

class simulation.results_aggregator.Results_Aggregator(sample_size, store_results=False)

   Bases: "object"

   aggregates results over the course of many simulation runs.
   performs various calculations automatically to streamline the
   process of displaying this information.

   add_result(simulation_results)

      adds a result to the results aggregator

      Parameters:
         **simulation_results** -- takes in a simulation results
         object from a single simulation run

   add_to_draw_totals(simulation_results)

   add_to_loss_totals(simulation_results)

   add_to_win_totals(simulation_results)

   calculate_averages(simulation_results)

      keeps a running calculation of the average number of defectors,
      skipped, invalid, and quit.

      Parameters:
         **simulation_results** -- results from a single simulation
         run

   calculate_maximums(simulation_results)

      keeps a running calculation of the maximum number of defectors,
      skipped, invalid, and quit.

      Parameters:
         **simulation_results** -- results from a single simulation
         run

   calculate_minimums(simulation_results)

      keeps a running calculation of the minimum number of defectors,
      skipped, invalid, and quit.

      Parameters:
         **simulation_results** -- results from a single simulation
         run

   calculate_secondaries()

      calculates internal member variables

   get_string() -> str

      Returns a string for displaying the results to the user

      Returns:
         string in displayable format


simulation.role_assignment module
=================================

simulation.role_assignment.role_assignment(env_vars, user_list, num_members_in_four_member_group)

   Assigns users to appropriate roles based on environment variable
   parameters

   Parameters:
      * **env_vars** -- environment variables for this simulation run

      * **user_list** -- list of users for this simulation run

      * **num_members_in_four_member_groups** -- number of users who
        were assigned into four member groups

simulation.role_assignment.test_role_assignment(b_printAllRoles)


simulation.sf4_invalidate_subgroups module
==========================================

simulation.sf4_invalidate_subgroups.sf4_invalidate_subgroups(sys_rec, user_list)

   Invalidates subgroups that are an invalid size. Alters appropriate
   variables in user records and system record.

   Parameters:
      * **sys_rec** -- simulation system record

      * **user_list** -- simulation user list


simulation.sf7_reorganization_of_users module
=============================================

simulation.sf7_reorganization_of_users.combine_groups(group1, group2)

simulation.sf7_reorganization_of_users.combine_size(group_list, group_size, potential_sizes, reorged=None)

   helper function for sf7 combining algorithm. Combines members in a
   group of size group_size with groups in potential sizes,
   prioritizing groups of size potential_sizes[i] over
   potential_sizes[i+1].

   Parameters:
      * **group_list** -- list of all the groups

      * **group_size** -- size to combine

      * **potential_sizes** -- list of sizes to combine with, ordered
        from greatest to least priority

      * **reorged** -- Do not use this parameter. Used for the array
        that stores reorged users

   Returns:
      altered group list

class simulation.sf7_reorganization_of_users.group_data(group_num, group_size, indices=[])

   Bases: "object"

   encapsulates a group object. used for sf7 combining algorithm

simulation.sf7_reorganization_of_users.sf7_reorganization_of_users(env_vars, sys_rec, user_list, tracking=-1)

   system function 7 implementation. reorganizes users who are in an
   invalid group size.

   Parameters:
      * **env_vars** -- takes in the simulation environment variables

      * **sys_rec** -- takes in simulation's system record

      * **user_list** -- takes in simulation's user list

      * **tracking** -- unused optional parameter, leave this field
        blank

simulation.sf7_reorganization_of_users.test_combine_size()


simulation.sf8_determine_claims module
======================================

simulation.sf8_determine_claims.sf8_determine_claims(env_vars, user_list)

   System function 8, determine claims based on chance_of_claim

   Parameters:
      * **env_vars** -- takes in environment variables for this
        simulation run

      * **user_list** -- takes in list of users for this simulation
        run


simulation.simulation module
============================

simulation.simulation.base_simulation(env_vars, sys_rec, pricing_vars, user_list, func=None)

   internal function for running the base simulation.

   Parameters:
      * **env_vars** -- environment variables to run the simulation
        with

      * **sys_rec** -- system record to initialize the simulation with

      * **pricing_vars** -- pricing variables to run the simulation
        with

      * **user_list** -- list of users to run the simulation with

      * **func** -- optional callback function to take snapshots of
        the simulation between periods

   Returns:
      simulation_results object detailing the results of the
      simulation run

simulation.simulation.exec_simulation(env_vars, pricing_vars, func=None) -> Simulation_Results

   Executes the simulation once, returns a Simulation_Results object
   that details the results of this individual run

   Parameters:
      * **env_vars** -- Environment variables to run the simulation
        with

      * **pricing_vars** -- Pricing variables to run the simulation
        with

      * **func** -- Optional callback function to record simulation
        variables between periods

   Returns:
      simulation_results, which details the results of this individual
      run

simulation.simulation.exec_simulation_debug(env_vars, pricing_vars)

   executes a debug run of the simulation. results in two CSVs being
   generated which contain information about the system record and
   user record between each period of a single simulation run.

   Parameters:
      * **env_vars** -- takes in the environment variables for this
        simulation run

      * **pricing_vars** -- takes in the pricing variables for this
        simulation run

   Returns:
      dict containing 'result', a string detailing the results of this
      individual simulation run. 'sys_csv_path', absolute path where
      the csv file detailing the system record is stored.
      'user_csv_path' absolute path where the csv file detailing the
      user record per period is stored.

simulation.simulation.exec_simulation_multiple(env_vars, pricing_vars, n) -> Results_Aggregator

   Executes the simulation multiple times and returns a
   Results_Aggregator object that details the results of these
   simulation runs.

   Parameters:
      * **env_vars** -- takes in simulation environment variables

      * **pricing_vars** -- takes in simulation pricing variables

      * **n** -- takes in number of trials to run the simulation for

   Returns:
      results_aggregator detailing results of *n* simulation runs

simulation.simulation.take_snapshot(simulation_results, sys_rec, add_skipped=True)


simulation.simulation_results module
====================================

class simulation.simulation_results.ResultsEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   Has 6 states: WIN_A, WIN_B, DRAW_A, DRAW_B, LOSS_A, LOSS_B, each of
   which indicates the results of a simulation, but also the reason
   that triggered the win/loss/draw (reason A or reason B?)

   DRAW_A = 2

   DRAW_B = 3

   LOSS_A = 4

   LOSS_B = 5

   WIN_A = 0

   WIN_B = 1

   static get_result_str(result)

class simulation.simulation_results.Simulation_Results

   Bases: "object"

   stores a results enum with some additional information


simulation.subgroup_setup module
================================

simulation.subgroup_setup.subgroup_setup(total_member_cnt, user_list)

   Assigns the users to their subgroups

   Parameters:
      * **total_member_cnt** -- total number of members we have in
        this simulation instance

      * **user_list** -- user list  for this simulation instance

   Returns:
      tuple containing (num_four_member_groups,
      num_five_member_groups, num_six_member_groups,
      num_seven_member_groups)

simulation.subgroup_setup.test_subgroup_setup()

simulation.subgroup_setup.test_subgroup_setup_basic_print()


simulation.system_record module
===============================

class simulation.system_record.System_Record(total_member_cnt)

   Bases: "object"

   stores system record variables for a simulation run

   calculate_vars()

   property claimed

   property defected_cnt

   property defection_shortfall

   property first_premium_calc

   property invalid_cnt

   property invalid_shortfall

   property quit_cnt

   property reorged_cnt

   property shortfall_credit_individual

   property shortfall_credit_total

   property shortfall_debt_individual

   property shortfall_debt_total

   property skip_shortfall

   property skipped_cnt

   property valid_remaining


simulation.uf1_determine_defectors module
=========================================

simulation.uf1_determine_defectors.test_uf1_determine_defectors(debugPrint=True)

simulation.uf1_determine_defectors.uf1_determine_defectors(env_vars, sys_record, user_list)

   user function 1; determines the defectors for this simulation run

   Parameters:
      * **env_vars** -- environment variables for this simulation run

      * **sys_record** -- system record for this simulation run

      * **user_list** -- list of users for this simulation run


simulation.uf2_pricing_function module
======================================

simulation.uf2_pricing_function.evaluate_cumulative(ev, pv, user, cur_period) -> bool

   evaluates cumulative increase to determine if user defects

   Parameters:
      * **ev** -- environment variables for this simulation run

      * **user** -- user to evaluate

      * **floor** -- floor to calculate threshold from

      * **cur_period** -- current period simulation is on

   Returns:
      true if they defect

simulation.uf2_pricing_function.evaluate_noref(ev, pv, user, cur_period) -> bool

   evaluates member who did not get a refund

   Parameters:
      * **ev** -- environment variables for this simulation run

      * **user** -- user to evaluate

      * **floor** -- floor to calculate threshold from

      * **cur_period** -- current period simulation is on

   Returns:
      true if they defect

simulation.uf2_pricing_function.evaluate_qualifying(ev, user, floor, cur_period)

   evaluates if member is qualifying to be evaluated for uf2

   Parameters:
      * **ev** -- environment variables for this simulation run

      * **user** -- user to evaluate

      * **floor** -- floor to calculate threshold from

      * **cur_period** -- current period simulation is on

   Returns:
      threshold < second premium calc

simulation.uf2_pricing_function.evaluate_refund(ev, pv, user, cur_period) -> bool

   Unused function. disabled per Josh's recommendation to improve
   simulation results

simulation.uf2_pricing_function.find_previous_matching_refund(user, cur_period) -> int

simulation.uf2_pricing_function.uf2_pricing_function(ev, sr, pv, user_list, cur_period)

   user function 2; pricing function

   Parameters:
      * **ev** -- takes in simulation environment variables

      * **sr** -- takes in simulation system record

      * **pv** -- takes in simulation pricing variables

      * **user_list** -- takes in user list for this simulation
        instance

      * **cur_period** -- current period the simulation is on


simulation.uf6_user_quit_function module
========================================

simulation.uf6_user_quit_function.increment_other_group_member_sbg_reorg_cnt(user_list, index)

simulation.uf6_user_quit_function.uf6_user_quit_function(env_vars, sys_rec, user_list)

   Determines users that quit

   Parameters:
      * **env_vars** -- environment variables for this simulation run

      * **sys_rec** -- system record for this simulation instance

      * **user_list** -- list of users for this simulation instance


simulation.user_record module
=============================

class simulation.user_record.CurrentStatusEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   DEFECTED = 1

   NR = 6

   PAID = 0

   PAID_INVALID = 3

   QUIT = 4

   REORG = 5

   SKIPPED = 2

class simulation.user_record.PayableEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   NO = 1

   NR = 2

   YES = 0

class simulation.user_record.PrimaryRoleEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   DEFECTOR = 0

   LOW_MORALE = 1

   UNITY = 2

class simulation.user_record.SecondaryRoleEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   DEPENDENT = 0

   INDEPENDENT = 1

class simulation.user_record.User_Record(env_vars)

   Bases: "object"

   User record stores the variables associated with a single user

   property credit_to_savings_account

class simulation.user_record.ValidityEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   INVALID = 1

   NR = 2

   VALID = 0

# Statistics Docs

statistics package
******************


Submodules
==========


statistics.confidence_interval module
=====================================

statistics.confidence_interval.calculate_confidence_interval(mean, std_dev, sample_size, alpha)

   Calculate the confidence interval for a given mean, standard
   deviation, sample size, and alpha level.

   Parameters: - mean: The sample mean - std_dev: The sample standard
   deviation - sample_size: The size of the sample - alpha: The alpha
   level for the confidence interval

   Returns: - (lower_bound, upper_bound): The lower and upper bounds
   of the confidence interval


statistics.hypothesis_test module
=================================

class statistics.hypothesis_test.TestTypeEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)

   Bases: "Enum"

   GREATER = 1

   LESS = 2

   TWOTAILED = 0

statistics.hypothesis_test.perform_hypothesis_test(mean, std_dev, sample_size, null_value, test_type)

   Perform a hypothesis test for the given mean, standard deviation,
   sample size, null value, and test type.

   Parameters: - mean: The sample mean - std_dev: The sample standard
   deviation - sample_size: The size of the sample - null_value: The
   value under the null hypothesis - test_type: Type of test
   (TWOTAILED, GREATER, LESS from TestTypeEnum)

   Returns: - p_value: The p-value of the test


statistics.searching module
===========================

class statistics.searching.Result(results_aggregator, attribute, value)

   Bases: "object"

class statistics.searching.Searching(ev, pv, ov)

   Bases: "object"

   implements the siulation search functionality

   basic_search(attribute: str, min_value, max_value, steps)

   get_linreg(attribute: str, min_value: float, max_value: float, steps: int, order: int)

   perform_full_search(attribute, target_percent, outcome, min_value, max_value, steps, order)

      Performs a search.

      Parameters:
         * **attribute** -- attribute to search

         * **target_percent** -- percent of <outcome> you want to
           target

         * **outcome** -- outcome you're studying (win, loss, or tie?)
           should be an OutcomeEnum object.

         * **min_value** -- minimum value to search (searches in
           [min_value, max_value])

         * **max_value** -- maximum value to search (searches in
           [min_value, max_value])

         * **steps** -- number of steps to search over and make a
           regression model from

         * **order** -- what order regression model to use? (e.g.
           order=2 will use L(x) = ax^2 + bx + c)

      Returns:
         a formatted string detailing the results in a displayable
         manner


statistics.searching_attributes module
======================================


statistics.statistics_aggregator module
=======================================

class statistics.statistics_aggregator.Statistics_Aggregator(ov)

   Bases: "object"

   Aggregates data for a simulation statistics run

   add_result(result: Results_Aggregator)

   calculate_confidence_intervals()

   calculate_hypothesis_test(attribute: str, null_value: float, test_type: TestTypeEnum)

   calculate_stats()

   get_string()

   print_dicts()


statistics.statistics_attributes module
=======================================


statistics.statistics_runner module
===================================

class statistics.statistics_runner.Statistics_Runner(ev, pv, ov)

   Bases: "object"

   Contains functionality for simulation statistics runs

   get_string()

      returns the statistics results as a formatted string

   run(hypothesis_tests=None)

      Runs statistics on the simulation.

# Utility

util package
************


Submodules
==========


util.ini_handler module
=======================

class util.ini_handler.INI_Handler(path)

   Bases: "object"

   Helper class for writing to INI config files

   read_environment_variables()

   read_other_variables()

   read_pricing_variables()

   write_environment_variables(ev)

   write_other_variables(ov)

   write_pricing_variables(pv)


util.results_db module
======================

class util.results_db.Results_DB(db_path='data/history.db')

   Bases: "object"

   Helper class for storing results in a database

   add_result(title, version, contents)

   create_table()

   get_result_by_id(result_id)

   get_results()

   set_remote_db(host, user, password, database)
