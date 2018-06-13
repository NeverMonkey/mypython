#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 17:05:19
# @Author  : taihou.nie (nevermonkey@126.com)
# @Link    : https://github.com/NeverMonkey
# @Host    : HP


def checkio(data):
    if len(data) > 9:
        if any(i.isupper() for i in data) \
                and any(i.islower() for i in data) \
                and any(i.isdigit() for i in data):
            return True
        else:
            return False
    else:
        return False
# checkio = lambda s: not(
#         len(s) < 10
#         or s.isdigit()
#         or s.isalpha()
#         or s.islower()
#         or s.isupper()
#     )
# Some hints
# Just check all conditions


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('bAse730onE4') == True, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
