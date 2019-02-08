# -*- coding: utf-8 -*-

from application_business_rules.interface_input_output import IEditStringUseCase


class Controller:

    def __init__(self, input_port : IEditStringUseCase):
        self.__input_port = input_port

    def execute(self, source : list)->None:
        self.__input_port.handle(source)
