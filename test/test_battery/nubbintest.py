import unittest
from datetime import date

from  battery.nubbin_battery import NubbinBattery

class NubbinTest(unittest.TestCase):
    def test_need_service(self):
        current_date = date.fromisoformat('2023-08-05')
        last_service_date = date.fromisoformat('2019-01-12')
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

        def test_dont_service(self):
            current_date = date.fromisoformat('2023-08-05')
            last_service_date = date.fromisoformat('2022-01-30')
            battery = NubbinBattery(current_date, last_service_date)
            self.assertFalse(battery.needs_service())