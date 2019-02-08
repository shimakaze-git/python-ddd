# -*- coding: utf-8 -*-
from injector import inject
from application_business_rules.interface_input_output import IEditStringUseCase


class Controller:
    @inject
    def __init__(self, input_port : IEditStringUseCase):
        self.__input_port = input_port

    def execute(self, source : list)->None:
        self.__input_port.handle(source)
