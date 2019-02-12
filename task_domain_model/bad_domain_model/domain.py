import enum
import datetime


class TaskStatus(enum.IntEnum):
    UNDONE = 0
    DONE = 1

class Task:

    POSTPONE_MAX_COUNT = 3

    def __init__(self):
        self.id = None
        self.task_status = None
        self.name = None
        self.due_date = None
        self.postpone_count = None

    """ setter """
    def set_id(self, id : int)->None:
        self.id = id

    def set_task_status(self, task_status : TaskStatus)->None:
        self.task_status = task_status

    def set_name(self, name : str)->None:
        self.name = name

    def set_due_date(self, due_date : datetime.datetime)->None:
        self.due_date = due_date

    def set_postpone_count(self, postpone_count : int)->None:
        self.postpone_count = postpone_count

    """ getter """
    def get_id(self)->int:
        return self.id

    def get_name(self)->str:
        return self.name

    def get_task_status(self)->TaskStatus:
        return self.task_status

    def get_due_date(self)->datetime.datetime:
        return self.due_date

    def get_postpone_count(self)->int:
        return self.postpone_count



    def can_postpone(self)->bool:
        return self.postpone_count < self.POSTPONE_MAX_COUNT