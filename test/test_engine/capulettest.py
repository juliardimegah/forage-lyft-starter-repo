import unittest

from engine.capulet_engine import CapuletEngine

class CapuletTest(unittest.TestCase):
    def test_need_service(self):
        mileage_now = 30001
        mileage_last_service = 0
        engine = CapuletEngine(mileage_now, mileage_last_service)
        self.assertTrue(engine.needs_service())


    def test_dont_service(self):
        mileage_now = 259800
        mileage_last_service = 224800
        engine = CapuletEngine(mileage_now, mileage_last_service)
        self.assertFalse(engine.needs_service())