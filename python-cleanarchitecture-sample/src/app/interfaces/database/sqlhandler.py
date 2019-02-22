#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Row(metaclass=ABCMeta):

    @abstractmethod
    def scan(self):
        pass

    @abstractmethod
    def _next(self):
        pass

    @abstractmethod
    def close(self):
        pass

class Result(metaclass=ABCMeta):

    @abstractmethod
    def last_insert_id(self)->int:
        pass

    @abstractmethod
    def rows_affected(self)->int:
        pass


class SqlHandler(metaclass=ABCMeta):

    @abstractmethod
    def execute(self)->Result:
        pass

    @abstractmethod
    def query(self):
        pass
