# -*- coding: utf-8 -*-
import os

class ConsolePresenter:

    def emit(self, data : str)->None:
        print(data)

class SaveToFilePresenter:
    __FILE_PATH = "out.txt"

    def emit(self, data : str)->None:
        file = open(self.__FILE_PATH, 'w')
        file.write(data)
        file.close()
