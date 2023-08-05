import unittest

from engine.willoughby_engine import WilloughbyEngine

class WilloughbyTest(unittest.TestCase):
    def test_need_service(self):
        mileage_now = 60001
        mileage_last_service = 0
        engine = WilloughbyEngine(mileage_now, mileage_last_service)
        self.assertTrue(engine.needs_service())


    def test_dont_service(self):
        mileage_now = 70000
        mileage_last_service = 60000
        engine = WilloughbyEngine(mileage_now, mileage_last_service)
        self.assertFalse(engine.needs_service())