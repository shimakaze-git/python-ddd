# datetime.date
from datetime import date


class User:
    def __init__(
        self,
        id: int,
        name: str,
        created_at: date,
        updated_at: date
    ):
        self.__id = id
        self.__name = name
        self.__created_at = created_at
        self.__updated_at = updated_at

    def to_json(self):
        return {
            'id': self.__id,
            'name': self.__name,
            'created_at': self.__created_at,
            'updated_at': self.__updated_at
        }
