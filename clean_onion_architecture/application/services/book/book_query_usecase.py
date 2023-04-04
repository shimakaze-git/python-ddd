# from flow_of_control.applications.interfaces import InterfaceUsecaseEditTextInputPort, InterfaceUsecaseEditTextOutputPort
from clean_onion_architecture.application.services.book.interface_book_usecase import InterfaceBookUseCase
from clean_onion_architecture.application.dto.book_dto import BookInputData, BookOutputData

from clean_onion_architecture.domain.model.book.entity import Book
from clean_onion_architecture.domain.model.book.exception import BookNotFoundError
from clean_onion_architecture.domain.model.book.repository import InterfaceBookRepository


class BookQueryUsecase(InterfaceBookUseCase):
    """"""
    _repository: InterfaceBookRepository

    def __init__(self, repository: InterfaceBookRepository) -> None:
        self._repository = repository

    def fetch_book_by_id(self, input_data: BookInputData) -> BookOutputData | None:
        """"""

        # input_data.id

        # find_by_id

        # raise NotImplementedError

        try:
            pass
            # book = self.book_query_service.find_by_id(id)
            # if book is None:
            #     raise BookNotFoundError
            book: Book | None = self._repository.find_by_id(id=input_data.id)
            if not book:
                raise BookNotFoundError
        except BookNotFoundError as e:
            raise e
        except Exception as e:
            raise e
        return BookOutputData(id=book.id, isbn="", title="")

    # @abstractmethod
    # def fetch_books(self) -> list[BookOutputData]:
    #     raise NotImplementedError
