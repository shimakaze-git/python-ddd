# -*- coding: utf-8 -*-

class FullName:

    def __init__(self, first_name: str, family_name : str):
        self.__first_name = first_name
        self.__family_name = family_name

    def first_name(self):
        return self.__first_name

    def family_name(self):
        return self.__family_name

def main():

    full_name1 = FullName("taro", "tanaka")
    print(full_name1.family_name())
    # tanaka

    full_name2 = FullName("john", "smith")
    print(full_name2.family_name())
    # smith

    # fullname = "tanaka taro";
    # tokens = fullname.split(' ');
    # familyname = tokens[0]
    # print(familyname)

if __name__ == '__main__':
    main()