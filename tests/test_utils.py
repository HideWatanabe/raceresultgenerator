import unittest
from datetime import timedelta
from unittest.mock import MagicMock, Mock
from utils import utils


class test_utils(unittest.TestCase):
    def test_format_time(self):
        mock_time = "0:04:15.578000"
        seconds = 255
        microseconds = 578000
        expected_time = "4:15.578"
        # time = timedelta.strptime(mock_time,"%H:%M:%S.%f")
        time = timedelta(seconds=seconds, microseconds = microseconds)
        print(time)
        result_time = utils.format_time(time)
        self.assertEqual(expected_time,result_time)

    def test_format_decimal(self):
        mock_value = 44.24600000000
        expected_value = "44.246"
        result = utils.format_decimal(mock_value)
        self.assertEqual(expected_value, result)
