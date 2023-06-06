import unittest


class TestPricingFunction(unittest.TestCase):

    def test_one_month_increase_percentage(self):
        # Assuming the function pricing_function returns a dictionary with the variables
        result = pricing_function()
        # Check if one_month_increase_percentage never exceeds prem_inc_ceiling
        self.assertLessEqual(result['one_month_increase_percentage'], result['prem_inc_ceiling'])

    def test_ph_skip_percentage(self):
        # Assuming the function pricing_function returns a dictionary with the variables
        result = pricing_function()
        # Check if ph_skip_percentage never exceeds ph_leave_ceiling
        self.assertLessEqual(result['ph_skip_percentage'], result['ph_leave_ceiling'])


if __name__ == '__main__':
    unittest.main()
