from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def fetch_data(self):
        pass
