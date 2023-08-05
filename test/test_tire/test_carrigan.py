import unittest

from tire.carrigan import Carrigan

class carrigantest(unittest.TestCase):
    def need_service(self):
        tire_wear = [0.1, 0.3, 0.2, 0.9]
        tire = Carrigan(tirewear)
        self.assertTrue(tire.needs_service())

    def dont_service(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tire = Carrigan(tirewear)
        self.assertFalse(tire.needs_service())