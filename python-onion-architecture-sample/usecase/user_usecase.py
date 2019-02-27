#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from domain.model.user_model import User
from domain.repository.user_repository import IFUserRepository

# UserUseCase interfase
class IFUserUseCase(metaclass=ABCMeta):
    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def get_user(self):
        pass

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def delete_user(self):
        pass


def new_user_usecase(repository: IFUserRepository)->IFUserUseCase:
    user_usecase = UserUseCase(repository)
    return user_usecase


class UserUseCase(IFUserUseCase):
    repository = None

    def __init__(self, user_repository: IFUserRepository):
        self.user_repository = user_repository

    def get_users(self)->User:
        return self.user_repository.fetch()

    def get_user(self, id: int)->User:
        return self.user_repository.fetch_by_id(id)

    def create_user(self, user: User)->User:
        return self.user_repository.create(user)

    def update_user(self, id: int)->User:
        user = self.user_repository.fetch_by_id(id)
        if user is None:
            pass
        return self.user_repository.update(user)

    def delete_user(self, id: int):
        return self.user_repository.delete(id)
