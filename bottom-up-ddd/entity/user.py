# -*- coding: utf-8 -*-

class FullName:

    def __init__(self, first_name: str, family_name : str):
        self.__first_name = first_name
        self.__family_name = family_name

    def first_name(self):
        return self.__first_name

    def family_name(self):
        return self.__family_name

# public class User {
#   private readonly UserId id;
#   private FullName name;

#   // データベース等から読み取ったときに利用するコンストラクタ
#   public User(UserId id, FullName name) {
#     this.id = id;
#     this.name = fullname;
#   }
  
#   // 生成するときのコンストラクタ（guid が設定される）
#   public User(FullName name){
#     this.id = new UserId(Guid.NewGuid().ToString());
#     this.name = name;
#   }

#   public void ChangeName(FullName newName) {
#     if (newName == null) throw new ArgumentNullException(nameof(newName));
#     name = newName;
#   }
# }

class User:
    def __init__(self, id: UserId, full_name: FullName):
        if not isinstance(full_name, FullName):
            raise Exception("full_name is not FullName.")
        self.__full_name = full_name
    
    def change_name(self, new_name: FullName):
        if new_name is None:
            raise Exception
        self.__full_name = new_name

class UserId:
    def __init__(self, id : str):
        self._value = id

    def value(self):
        return self._value

    def __eq__(self, other: User):
        if isinstance(other, User):
            if other is None:
                return False
    
            if other is self:
                return True
            return self._value == other._value
        else:
            if other is None:
                return False
    
            if other is self:
                return True

            if type(other) is not type(self):
                return False
            return isinstance(other, User)

def main():

    full_name1 = FullName("taro", "tanaka")
    print(full_name1.family_name())
    # tanaka

    full_name2 = FullName("john", "smith")
    print(full_name2.family_name())
    # smith

    user = User(None)
    # user.change_name(None)
    
    # userid = UserId(str(1))
    # print(userid._value)

if __name__ == '__main__':
    main()