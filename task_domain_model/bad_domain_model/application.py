import datetime

from .domain import Task, TaskStatus
from .repository import TaskRepository


class TaskApplication:

    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, name : str, due_date : datetime.datetime)->None:
        if (name is None) or (due_date is None):
            raise Exception("必須項目が設定されていません")
        task = Task()
        task.set_task_status(TaskStatus.UNDONE)
        task.set_name(name)
        task.set_due_date(due_date)
        task.set_postpone_count(0)

        self.task_repository.save(task)

    def postpone_task(self, task_id : int)->None:
        task = self.task_repository.find_by_id(task_id)
        if (task.can_postpone() is False):
            raise Exception("最大延期回数を超過しています")

        due_date = task.get_due_date() + datetime.timedelta(days=11)
        task.set_due_date(due_date)

        task.set_postpone_count(task.get_postpone_count() + 1)
        self.task_repository.save(task)


class AnotherTaskApplication:

    def __init__(self):
        self.task_repository = TaskRepository()

    def create_done_task(self, name : str, due_date):
        task = Task()

        # × 完了状態でタスク生成
        task.set_task_status(TaskStatus.DONE)
        
        # × カウントがまさかのマイナス
        task.set_postpone_count(-1)
        self.task_repository.save(task)

    def change_task(self, task_id : int, name : str, due_date : datetime.datetime, task_status):
        task = self.task_repository.find_by_id(task_id)

        # × 変更してはいけないタスク名を変更
        task.set_name(name)

        # × 勝手に期日を入力値で設定、延期回数も無視
        task.set_due_date(due_date)
        
        # × タスクを未完了に戻せてしまう
        task.set_task_status(task_status)
        self.task_repository.save(task)
