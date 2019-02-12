import datetime

from .domain import Task
from .repository import TaskRepository

class TaskApplication:

    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, name : str, due_date : datetime.datetime):
        # taskインスタンスは、常に不変条件を満たした形で生成される
        task = Task(name, due_date)
        self.task_repository.save(task)

    def postpone(self, task_id : int)->None:
        task = self.task_repository.find_by_id(task_id)

        # 取得したオブジェクトに対して、不変条件を破壊するような処理はapplicationから書くことができない
        task.postpone()
        self.task_repository.save(task)

    # 完了処理は略
    #バリデーションは略