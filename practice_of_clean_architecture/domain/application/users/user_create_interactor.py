#!/usr/bin/python
'''
Created on 2019/2/11
@author: shimakaze-git
'''
import os
import sys
import json

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        )
    )
)

from domain.domain.users.user import User


class UserCreateInteractor:
    # def __init__(self, user_repository : IUserRepository):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    # def handle(self, request : UserCreateRequest):
    def handle(self, request):
        username = request.user_name
        duplicate_user = self.user_repository.find_by_user_name(username)

        if(duplicate_user is not None):
            raise Exception("duplicated")

        user = User(username)
        self.user_repository.save(user)
