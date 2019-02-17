# -*- coding: utf-8 -*-


class FullName:
    """"
    イミュータブル（Immutable, 不変）なクラス: FullName
    """

    def __init__(self, first_name: str, family_name: str):
        self.__first_name = first_name
        self.__family_name = family_name

    # getter
    def first_name(self):
        return self.__first_name

    def family_name(self):
        return self.__family_name

    # setter
    def change_family_name(family_name: str):
        self.__family_name = family_name

    def change_first_name(first_name: str):
        self.__first_name = family_name
