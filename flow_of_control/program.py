# # -*- coding: utf-8 -*-

# from interface_adapters.controller import Controller
# from interface_adapters.presenter import ConsolePresenter, SaveToFilePresenter

# from application_business_rules.usecase import ToCsvUseCase, ToTsvUseCase
# from application_business_rules.interface_input_output import IEditStringUseCase, IEditStringOutputPort

# from injector import Injector, inject, Module


# class Program():
#     data = ["source", "data", "foo", "bar"]

#     @classmethod
#     def console_csv_usecase(self):
#         output_port = ConsolePresenter()
#         interactor = ToCsvUseCase(output_port)
#         controller = Controller(interactor)
#         controller.execute(self.data)

#     @classmethod
#     def save_to_file_csv_usecase(self):
#         output_port = SaveToFilePresenter()
#         interactor = ToCsvUseCase(output_port)
#         controller = Controller(interactor)
#         controller.execute(self.data)

#     @classmethod
#     def console_tsv_usecase(self):
#         output_port = ConsolePresenter()
#         interactor = ToTsvUseCase(output_port)
#         controller = Controller(interactor)
#         controller.execute(self.data)

#     @classmethod
#     def save_to_file_tsv_usecase(self):
#         output_port = SaveToFilePresenter()
#         interactor = ToTsvUseCase(output_port)
#         controller = Controller(interactor)
#         controller.execute(self.data)


# class DIContainer(Module):
#     def configure(self, binder):
#         binder.bind(IEditStringOutputPort, to=ConsolePresenter)
#         binder.bind(IEditStringUseCase, to=ToCsvUseCase)

#         # binder.bind(IEditStringOutputPort, to=SaveToFilePresenter)
#         # binder.bind(IEditStringUseCase, to=ToTsvUseCase)

# def register_dependency():
#     injector = Injector([DIContainer()])
#     controller = injector.get(Controller)
#     controller.execute(Program.data)


# def main():
#     # Program.console_csv_usecase()
#     # Program.save_to_file_csv_usecase()
#     # Program.console_tsv_usecase()
#     # Program.save_to_file_tsv_usecase()

#     register_dependency()


# if __name__ == "__main__":
#     main()
