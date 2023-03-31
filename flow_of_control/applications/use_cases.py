# from injector import inject
from interfaces import InterfaceUsecaseEditTextInputPort, InterfaceUsecaseEditTextOutputPort


class ToCsvUseCaseInteractor(InterfaceUsecaseEditTextInputPort):
    """"""
    output_port: InterfaceUsecaseEditTextOutputPort

    # @inject
    def __init__(self, output_port: InterfaceUsecaseEditTextOutputPort) -> None:
        """"""
        self.output_port = output_port

    def handle(self, text_list: list[str]) -> None:
        """"""

        text: str = ",".join(text_list)
        self.output_port.emit(text)


class ToTsvUseCaseInteractor(InterfaceUsecaseEditTextInputPort):
    """"""
    output_port: InterfaceUsecaseEditTextOutputPort

    # @inject

    def __init__(self, output_port: InterfaceUsecaseEditTextOutputPort):
        self.output_port = output_port

    def handle(self, text_list: list[str]) -> None:
        """"""

        text: str = "\t".join(text_list)
        self.output_port.emit(text)
