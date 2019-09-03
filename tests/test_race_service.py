import unittest
from unittest.mock import Mock, MagicMock, patch
import datetime
from service import race_service
from model.models import Race, Pilot, Lap
from repository import file_repository

class test_race_service(unittest.TestCase):

    def setUp(self):
        pilot = Pilot('038','F.MASSA')
        self.mocked_race = Race(pilot)
        mocked_laps = ["23:49:08.277      038 – F.MASSA                           1		1:02.852                        44,275",
            "23:50:11.447      038 – F.MASSA                           2		1:03.170                        44,053",
            "23:51:14.216      038 – F.MASSA                           3		1:02.769                        44,334",
            "23:52:17.003      038 – F.MASS                            4		1:02.787                        44,321"]
        laps = []
        for lap in mocked_laps:
            laps.append(Lap(lap.split()))
        self.mocked_race.extend_lap(laps)

    def test_get_race_time(self):
        # 0:04:11.578000
        expected = datetime.timedelta(minutes = 4,
            seconds = 11, microseconds = 578000)

        laps = race_service.get_race_time(self.mocked_race.laps)        
        self.assertEqual(expected,laps)
        pass

    def test_parse_file_calling_internal_methods(self):
        file_name = "teste"
        race_service.parse_file(file_name)
        Mock.assert_called(file_repository.get_file)

    def test_parse_file_data(self):
        file_repository.get_file = MagicMock(return_value=open("tests/mock.log"))
        file_name = "teste"
        race_results, pilots, best_lap = race_service.parse_file(file_name)
        self.assertEqual(2,len(race_results))
        self.assertEqual(2,len(pilots))
        #validating data
        self.assertIsNotNone(pilots["038"])
        self.assertIsNotNone(pilots["033"])
        with self.assertRaises(KeyError):
            self.assertIsNone(pilots["002"])

    def test_generate_result(self):
        file_repository.get_file = MagicMock(return_value=open("logs/karts.log"))
        result = race_service.generate_result()
        self.assertIsNotNone(result.races)
        self.assertEqual(6,len(result.races))
        self.assertEqual("038",result.races[0].pilot.code)
        self.assertEqual(4,len(result.races[0].laps))
        
    def test_generate_result_with_empty_list(self):
        file_repository.get_file = MagicMock(return_value=open("tests/empty.log"))
        result = race_service.generate_result()
        self.assertEqual(0,len(result.races))

    