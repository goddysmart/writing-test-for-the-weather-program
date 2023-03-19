import unittest
from program import show_weather_to_user

class TestShowWeatherToUser(unittest.TestCase):
    def test_single_day(self):
        weather_data_list = [{'timepoint': 24, 'temp2m': 20}]
        expected_output = "On day 24,\nThe temperature is 20\n"
        self.assertEqual(show_weather_to_user(weather_data_list), expected_output)

    def test_two_days(self):
        weather_data_list = [{'timepoint': 48, 'temp2m': 18}]
        expected_output = "On day 48,\n(in two days)\nThe temperature is 18\n"
        self.assertEqual(show_weather_to_user(weather_data_list), expected_output)

    def test_three_days(self):
        weather_data_list = [{'timepoint': 72, 'temp2m': 22}]
        expected_output = "On day 72,\n(in three days)\nThe temperature is 22\n"
        self.assertEqual(show_weather_to_user(weather_data_list), expected_output)

    def test_multiple_days(self):
        weather_data_list = [{'timepoint': 24, 'temp2m': 20},
                             {'timepoint': 48, 'temp2m': 18},
                             {'timepoint': 72, 'temp2m': 22}]
        expected_output = "On day 24,\nThe temperature is 20\nOn day 48,\n(in two days)\nThe temperature is 18\nOn day 72,\n(in three days)\nThe temperature is 22\n"
        self.assertEqual(show_weather_to_user(weather_data_list), expected_output)

if name == '__main__':
    unittest.main()
