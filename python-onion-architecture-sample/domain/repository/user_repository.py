from abc import ABCMeta, abstractmethod
from domain.model.user_model import User


class IFUserRepository(metaclass=ABCMeta):

    @abstractmethod
    def fetch(self)->User:
        pass

    @abstractmethod
    def fetch_by_id(self, id: int)->User:
        pass

    @abstractmethod
    def create(self, user)->User:
        pass

    @abstractmethod
    def update(self, user)->User:
        pass

    @abstractmethod
    def delete(self, id: int)->None:
        pass
