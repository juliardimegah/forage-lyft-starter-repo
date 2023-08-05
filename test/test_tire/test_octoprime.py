import unittest

from tire.octoprime import OctoPrime

class carrigantest(unittest.TestCase):
    def need_service(self):
        tire_wear = [0.8, 0.8, 0.8, 0.7]
        tire = OctoPrime(tirewear)
        self.assertTrue(tire.needs_service())

    def dont_service(self):
        tire_wear = [0.1, 0.2, 0.4, 0.2]
        tire = OctoPrime(tirewear)
        self.assertFalse(tire.needs_service())