# conding: utf-8
from abc import ABCMeta, abstractmethod

# class IFWriter(metaclass=ABCMeta):
#     @abstractmethod
#     def output(self, title : str, body : str):
#         pass


# package usecase

# import "app/domain"

# type UserRepository interface {
# 	Store(domain.User) (int, error)
# 	FindById(int) (domain.User, error)
# 	FindAll() (domain.Users, error)
# }



class IFUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def find_by_id(self, identifier: int):
        pass

    @abstractmethod
    def find_all(self):
        pass
