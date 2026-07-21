from abc import ABC, abstractmethod


class Visual(ABC):

    def __init__(self, datumset, *params):
        self.datumset = datumset
        self.params = params

    @abstractmethod
    def draw(self):
        pass
