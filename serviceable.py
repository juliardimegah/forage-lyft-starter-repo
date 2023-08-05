from abc import ABC


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass