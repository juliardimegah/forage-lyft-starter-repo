import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class cartestcase(unittest.TestCase):
    car_class = None

    def setUp(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        self.current_mileage = 0
        self.last_service_mileage = 0
        self.car = self.car_class(last_service_date, self.current_mileage, self.last_service_mileage)

    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        self.car.last_service_date = last_service_date
        self.assertTrue(self.car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        self.car.last_service_date = last_service_date
        self.assertFalse(self.car.needs_service())  

    def test_engine_should_be_serviced(self):
        self.car.current_mileage = 30001
        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.car.current_mileage = 30000
        self.assertFalse(self.car.needs_service())

class TestCalliope(cartestcase):
    car_class = Calliope

class TestGlissade(cartestcase):
    car_class = Glissade

class TestPalindrome(cartestcase):
    car_class = Palindrome
    
    def test_engine_should_be_serviced(self):
        self.car.warning_light_is_on = True
        self.assertTrue(self.car.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.car.warning_light_is_on = False
        self.assertFalse(self.car.needs_service())

class TestRorschach(cartestcase):
    car_class = Rorschach

class TestThovex(cartestcase):
    car_class = Thovex

if __name__ == '__main__':
    unittest.main()
