# -*- coding: utf-8 -*-

from application_business_rules.interface_input_output import IEditStringOutputPort


class ToCsvUseCase:

    def __init__(self, output_port : IEditStringOutputPort):
        self.__output_port = output_port

    def handle(self, data : list)->None:
        result = None
        result = ','.join(data)
        self.__output_port.emit(result)

class ToTsvUseCase:

    def __init__(self, output_port : IEditStringOutputPort):
        self.__output_port = output_port

    def handle(self, data : list)->None:
        result = '\t'.join(data)
        self.__output_port.emit(result)
