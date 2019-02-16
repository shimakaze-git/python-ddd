# class User:
#     def __init__(self, name : str):
#         self.name = name

#     def change_name(self, name : str):
#         self.name = name



# ユーザー名が3文字以上の制約を課した実装
# class User:
#     def __init__(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.name = name

#     def change_name(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.name = name


# 電話番号の登録と電話番号の形式が正しいかのチェック機構を加えた実装
# import re

# class User:
#     def __init__(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.name = name

#         self.phone_number = None

#     def change_name(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.name = name

#     def change_phone_number(self, phone_number : str):
#         pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         if result is None:
#             raise Exception('throw argument phone_number')
#         self.phone_number = phone_number


# 追加で企業情報のためのクラスを作り、Userと同じように電話番号を登録できるようにする
# import re

# class Company:
#     def __init__(self):
#         self.phone_number = None

#     def change_phone_number(self, phone_number : str):
#         pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         if result is None:
#             raise Exception('throw argument phone_number')
#         self.phone_number = phone_number


# 
# import re

# class User:
#     def __init__(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.name = name

#         self.phone_number = None

#     def change_name(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.name = name

#     def change_phone_number(self, phone_number : str):
#         pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         if result is None:
#             raise Exception('throw argument phone_number')
#         self.phone_number = phone_number

#     def is_mobile_phone(self):
#         pattern = '^(070|080|090)-\d{4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         return True if result is not None else False

# class Company:
#     def __init__(self):
#         self.phone_number = None

#     def change_phone_number(self, phone_number : str):
#         pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         if result is None:
#             raise Exception('throw argument phone_number')
#         self.phone_number = phone_number

#     def is_mobile_phone(self):
#         pattern = '^(070|080|090)-\d{4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         return True if result is not None else False



# class UserName:
#     def __init__(self, name : str):
#         if len(name) < 3:
#             raise Exception('throw argument name')
#         self.value = name

# class PhoneNumber:
#     def __init__(self, phone_number : str):
#         pattern = '^0\d{1,4}-\d{1,4}-\d{4}$'
#         result = re.match(pattern, phone_number)
#         if result is None:
#             raise Exception('throw argument phone_number')
#         self.full = phone_number

#     def is_mobile_phone(self):
#         pattern = '^(070|080|090)-\d{4}-\d{4}$'
#         result = re.match(pattern, self.full)
#         return True if result is not None else False
