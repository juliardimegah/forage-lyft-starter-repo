from tire.tire import Tire

class OctoPrime(Tire):
    def __init__(self, tirewear):
        self.tirewear = tirewear

    def needs_service(self):
        return self.tirewear >= 3