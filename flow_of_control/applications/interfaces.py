from abc import ABCMeta, abstractmethod


class InterfaceUsecaseEditTextInputPort(metaclass=ABCMeta):
    """"""

    @abstractmethod
    def handle(self, text_list: list[str]) -> None:
        raise NotImplementedError


class InterfaceUsecaseEditTextOutputPort(metaclass=ABCMeta):
    """"""

    @abstractmethod
    def emit(self, text: str) -> None:
        raise NotImplementedError
