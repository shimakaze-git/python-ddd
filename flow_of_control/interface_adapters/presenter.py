from applications.interfaces import InterfaceUsecaseEditTextOutputPort


class ConsolePresenter(InterfaceUsecaseEditTextOutputPort):
    """"""

    def emit(self, text: str) -> None:
        print("ConsolePresenter text", text)


class SaveToFilePresenter(InterfaceUsecaseEditTextOutputPort):
    __FILE_PATH: str = "out.txt"

    def emit(self, text: str) -> None:
        file = open(self.__FILE_PATH, 'w')
        file.write(text)
        file.close()
