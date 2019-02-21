import uuid

class User:

    def __init__(self, id : str, user_name : str):
        if id is None:
            id = str(uuid.uuid4())
        self.Id = id
        self.user_name = user_name
