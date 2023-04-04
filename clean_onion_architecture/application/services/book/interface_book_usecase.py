from abc import ABC, abstractmethod

from clean_onion_architecture.application.dto.book_dto import BookOutputData, BookInputData


class InterfaceBookUseCase(ABC):
    """"""

    @abstractmethod
    def fetch_book_by_id(self, input_data: BookInputData) -> BookOutputData | None:
        raise NotImplementedError

    @abstractmethod
    def fetch_books(self) -> list[BookOutputData]:
        raise NotImplementedError
