# using System.Collections.Generic;

# namespace Domain.Domain.Users {
#     public interface IUserRepository {
#         User Find(UserId id);
#         User Find(UserName name);
#         IEnumerable<User> FindAll();
#         void Save(User user);
#         void Remove(User user);
#     }
# }
# from 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


# 抽象クラス
class IUserRepository(metaclass=ABCMeta):

    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def find_all(self, id):
        pass

    @abstractmethod
    def save(self, id):
        pass

    @abstractmethod
    def remove(self, id):
        pass
