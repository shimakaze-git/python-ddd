# -*- coding: utf-8 -*-

class User:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    def change_name(self, name: str):
        self._name = name

    def is_equal_entity(self, other):
        return self._id == other._id

# class User{
#   public User(long id, string name){
#     Id = id;
#     Name = name;
#   }

#   public long Id { get; }
#   public string Name { get; private set; }

#   public void ChangeName(string name){
#     Name = name;
#   }

#   public bool IsEqualEntity(User other){
#     return Id == other.Id;
#   }
# }