import unittest
from unittest.mock import MagicMock, Mock
from repository import file_repository
import os

class test_file_repository(unittest.TestCase):
    def test_get_file_with_existing_file(self):
        file_name = "logs/karts.log"
        logs = file_repository.get_file(file_name)
        self.assertIsNotNone(logs)

    def test_get_file_without_existing_file(self):
        error_file_name = "logs/karts.loga"
        exc = None
        try:
            logs = file_repository.get_file(error_file_name)
        except(FileNotFoundError):
            exc = FileNotFoundError()
        self.assertIsNotNone(exc)

    def test_read_empty_file(self):
        file_repository.get_file = Mock(return_value=None)
        file_name = "logs/karts.log"
        logs = file_repository.read_file(file_name)
        Mock.assert_called(file_repository.get_file)
