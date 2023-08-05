import unittest

from engine.sternman_engine import SternmanEngine

class SternmanTest(unittest.TestCase):
    def test_need_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())


    def test_dont_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())