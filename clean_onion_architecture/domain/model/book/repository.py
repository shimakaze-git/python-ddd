from abc import ABC, abstractmethod

from clean_onion_architecture.domain.model.book.entity import Book


class InterfaceBookRepository(ABC):
    """"""

    @abstractmethod
    def create(self, book: Book) -> Book | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Book | None:
        raise NotImplementedError

    @abstractmethod
    def find_by_isbn(self, isbn: str) -> Book | None:
        raise NotImplementedError

    @abstractmethod
    def update(self, book: Book) -> Book | None:
        raise NotImplementedError

    @abstractmethod
    def delete_by_id(self, id: str) -> None:
        raise NotImplementedError
