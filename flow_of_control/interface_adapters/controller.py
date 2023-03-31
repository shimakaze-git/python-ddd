# from injector import inject
from applications.interfaces import InterfaceUsecaseEditTextInputPort


class Controller:
    """"""
    __input_port: InterfaceUsecaseEditTextInputPort

    def __init__(self, input_port: InterfaceUsecaseEditTextInputPort) -> None:
        self.__input_port = input_port

    def execute(self, text_list: list[str]) -> None:
        self.__input_port.handle(text_list)
