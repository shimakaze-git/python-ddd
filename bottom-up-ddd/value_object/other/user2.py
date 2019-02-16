
class UserName:
    def __init__(self, name: str):
        if len(name) < 3:
            raise Exception('throw argument name')
        self.value = name


class PhoneNumber:
    def __init__(self, phone_number: str):
        pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
        result = re.match(pattern, phone_number)
        if result is None:
            raise Exception('throw argument phone_number')
        self.full = phone_number

    def is_mobile_phone(self):
        pattern = '^(070|080|090)-\d{4}-\d{4}$'
        result = re.match(pattern, self.full)
        return True if result is not None else False


class User:
    def __init__(self, name: UserName):
        if name is None:
            raise Exception('ArgumentNullException name')
        self.name = name

    def change_name(self, name: UserName):
        if name is None:
            raise Exception('ArgumentNullException name')
        self.name = name

    def phone_number(self, phone_number: PhoneNumber):
        if phone_number is None:
            raise Exception('ArgumentNullException phone_number')
        self.phone_number = phone_number


class Company:
    def change_phone_number(self, phone_number: PhoneNumber):
        if phone_number is None:
            raise Exception('ArgumentNullException phone_number')
        self.phone_number = phone_number
