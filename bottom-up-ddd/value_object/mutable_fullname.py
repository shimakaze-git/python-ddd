# -*- coding: utf-8 -*-


class FullName:
    """"
    ミュータブル（mutable, 可変）なクラス: FullName
    """

    def __init__(self, first_name: str, family_name: str):
        self.__first_name = first_name
        self.__family_name = family_name

    # getter
    def first_name(self):
        return self.__first_name

    def family_name(self):
        return self.__family_name
