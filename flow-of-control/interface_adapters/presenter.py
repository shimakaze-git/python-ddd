# -*- coding: utf-8 -*-
import os

from application_business_rules.interface_input_output import IEditStringOutputPort

class ConsolePresenter(IEditStringOutputPort):

    def emit(self, data : str)->None:
        print(data)

class SaveToFilePresenter(IEditStringOutputPort):
    __FILE_PATH = "out.txt"

    def emit(self, data : str)->None:
        file = open(self.__FILE_PATH, 'w')
        file.write(data)
        file.close()
