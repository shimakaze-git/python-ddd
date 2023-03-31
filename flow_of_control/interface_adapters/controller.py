from injector import inject
from flow_of_control.applications.interfaces import InterfaceUsecaseEditTextInputPort


class Controller:
    """"""
    input_port: InterfaceUsecaseEditTextInputPort

    @inject
    def __init__(self, input_port: InterfaceUsecaseEditTextInputPort) -> None:
        self.input_port = input_port

    def execute(self, text_list: list[str]) -> None:
        self.input_port.handle(text_list)
