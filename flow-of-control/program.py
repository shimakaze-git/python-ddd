# -*- coding: utf-8 -*-

from interface_adapters.controller import Controller
from interface_adapters.presenter import ConsolePresenter, SaveToFilePresenter
from application_business_rules.usecase import ToCsvUseCase, ToTsvUseCase


class Program():
    data = ["source", "data", "foo", "bar"]

    @classmethod
    def console_csv_usecase(self):
        output_port = ConsolePresenter()
        interactor = ToCsvUseCase(output_port)
        controller = Controller(interactor)
        controller.execute(self.data)

    @classmethod
    def save_to_file_csv_usecase(self):
        output_port = SaveToFilePresenter()
        interactor = ToCsvUseCase(output_port)
        controller = Controller(interactor)
        controller.execute(self.data)

    @classmethod
    def console_tsv_usecase(self):
        output_port = ConsolePresenter()
        interactor = ToTsvUseCase(output_port)
        controller = Controller(interactor)
        controller.execute(self.data)

    @classmethod
    def save_to_file_tsv_usecase(self):
        output_port = SaveToFilePresenter()
        interactor = ToTsvUseCase(output_port)
        controller = Controller(interactor)
        controller.execute(self.data)

def main():

    Program.console_csv_usecase()
    Program.save_to_file_csv_usecase()
    Program.console_tsv_usecase()
    Program.save_to_file_tsv_usecase()

if __name__ == "__main__":
    main()