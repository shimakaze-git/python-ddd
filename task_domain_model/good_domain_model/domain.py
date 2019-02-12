import enum
import datetime


class TaskStatus(enum.IntEnum):
    UNDONE = 0
    DONE = 1


class Task:

    POSTPONE_MAX_COUNT = 3

    """"
    コンストラクタ : エンティティ作成時の不変条件を表現
    """
    def __init__(self, name : str, due_date : datetime.datetime):
        if (name is None) or (due_date is None):
            raise Exception("必須項目が設定されていません")

        self.id = None

        self.name = name
        self.due_date = due_date
        self.task_status = None
        self.postpone_count = 0;

    """"
    状態遷移メソッド：作成済みエンティティの状態遷移に関する不変条件を表現
    """
    def postpone(self)->None:
        if self.postpone_count >= self.POSTPONE_MAX_COUNT:
            raise Exception("最大延期回数を超過しています")
        self.due_date += datetime.timedelta(days=11)
        self.postpone_count += 1

    def done(self)->None:
        self.task_status = TaskStatus.DONE

    """" setterは実装してはいけない """

    """ getter """
    def get_id(self)->int:
        return self.id

    def get_name(self)->str:
        return self.name

    def get_task_status(self)->TaskStatus:
        return self.task_status

    def get_due_date(self)->datetime.datetime:
        return self.due_date

    def is_undone(self)->bool:
        return self.task_status == TaskStatus.UNDONE

    def can_postpone(self)->bool:
        return self.postpone_count < self.POSTPONE_MAX_COUNT
