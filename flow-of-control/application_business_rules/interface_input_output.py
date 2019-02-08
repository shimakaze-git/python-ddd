# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class IEditStringUseCase(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, data : list)->None:
        pass

class IEditStringOutputPort(metaclass=ABCMeta):
    @abstractmethod
    def emit(self, data : str)->None:
        pass
