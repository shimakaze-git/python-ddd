from injector import Injector, Module, Binder

from flow_of_control.interface_adapters.presenter import ConsolePresenter, SaveToFilePresenter
from flow_of_control.interface_adapters.controller import Controller

from flow_of_control.applications.interfaces import InterfaceUsecaseEditTextInputPort, InterfaceUsecaseEditTextOutputPort
from flow_of_control.applications.use_cases import ToCsvUseCaseInteractor, ToTsvUseCaseInteractor


class Program:
    data: list[str] = ["source", "data", "foo", "bar"]

    @classmethod
    def console_csv_usecase(cls) -> InterfaceUsecaseEditTextInputPort:
        """"""

        output_port: InterfaceUsecaseEditTextOutputPort = ConsolePresenter()
        interactor: InterfaceUsecaseEditTextInputPort = ToCsvUseCaseInteractor(output_port)
        controller: Controller = Controller(interactor)
        controller.execute(Program.data)

        return interactor

    @classmethod
    def save_to_file_csv_usecase(cls) -> InterfaceUsecaseEditTextInputPort:
        """"""
        output_port: InterfaceUsecaseEditTextOutputPort = SaveToFilePresenter()
        interactor: InterfaceUsecaseEditTextInputPort = ToCsvUseCaseInteractor(output_port)
        controller: Controller = Controller(interactor)
        controller.execute(Program.data)

        return interactor

    @classmethod
    def console_tsv_usecase(cls) -> InterfaceUsecaseEditTextInputPort:
        """"""

        output_port: InterfaceUsecaseEditTextOutputPort = ConsolePresenter()
        interactor: InterfaceUsecaseEditTextInputPort = ToTsvUseCaseInteractor(output_port)
        controller: Controller = Controller(interactor)
        controller.execute(Program.data)

        return interactor

    @classmethod
    def save_to_file_tsv_usecase(cls) -> InterfaceUsecaseEditTextInputPort:
        """"""

        output_port: InterfaceUsecaseEditTextOutputPort = SaveToFilePresenter()
        interactor: InterfaceUsecaseEditTextInputPort = ToTsvUseCaseInteractor(output_port)
        controller: Controller = Controller(interactor)
        controller.execute(Program.data)

        return interactor


def test_console_csv_usecase():
    """"""
    print("test_console_csv_usecase")

    class DIContainer(Module):
        def configure(self, binder: Binder):
            binder.bind(InterfaceUsecaseEditTextOutputPort, to=ConsolePresenter)
            binder.bind(InterfaceUsecaseEditTextInputPort, to=ToCsvUseCaseInteractor)

    interactor: InterfaceUsecaseEditTextInputPort = Program.console_csv_usecase()

    injector: Injector = Injector([DIContainer()])
    controller: Controller = injector.get(Controller)
    controller.execute(Program.data)

    assert str(type(interactor)) == str(type(controller.input_port))


def test_console_tsv_usecase():
    """"""
    print("test_console_tsv_usecase")

    class DIContainer(Module):
        def configure(self, binder: Binder):
            binder.bind(InterfaceUsecaseEditTextOutputPort, to=ConsolePresenter)
            binder.bind(InterfaceUsecaseEditTextInputPort, to=ToTsvUseCaseInteractor)

    interactor: InterfaceUsecaseEditTextInputPort = Program.console_tsv_usecase()

    injector: Injector = Injector([DIContainer()])
    controller: Controller = injector.get(Controller)
    controller.execute(Program.data)

    assert str(type(interactor)) == str(type(controller.input_port))


def test_save_to_file_csv_usecase():
    """"""
    print("test_save_to_file_csv_usecase")

    class DIContainer(Module):
        def configure(self, binder: Binder):
            binder.bind(InterfaceUsecaseEditTextOutputPort, to=SaveToFilePresenter)
            binder.bind(InterfaceUsecaseEditTextInputPort, to=ToCsvUseCaseInteractor)

    interactor: InterfaceUsecaseEditTextInputPort = Program.save_to_file_csv_usecase()

    injector: Injector = Injector([DIContainer()])
    controller: Controller = injector.get(Controller)
    controller.execute(Program.data)

    assert str(type(interactor)) == str(type(controller.input_port))


def test_save_to_file_tsv_usecase():
    """"""
    print("test_save_to_file_tsv_usecase")

    class DIContainer(Module):
        def configure(self, binder: Binder):
            binder.bind(InterfaceUsecaseEditTextOutputPort, to=SaveToFilePresenter)
            binder.bind(InterfaceUsecaseEditTextInputPort, to=ToTsvUseCaseInteractor)

    interactor: InterfaceUsecaseEditTextInputPort = Program.save_to_file_tsv_usecase()

    injector: Injector = Injector([DIContainer()])
    controller: Controller = injector.get(Controller)
    controller.execute(Program.data)

    assert str(type(interactor)) == str(type(controller.input_port))
