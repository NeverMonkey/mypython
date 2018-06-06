#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-20 18:05:52
# @Author  : taihou.nie (nevermonkey@126.com)
# @Link    : https://github.com/NeverMonkey
# @Host    : HP


def checkmost(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max([chr(i) for i in range(97, 123)], key=text.count)


# list(map(text.count, [chr(i) for i in range(97, 123)]))


def checkall(text):
    text = text.lower()
    return zip([chr(i) for i in range(97, 123)], list(map(text.count, [chr(i) for i in range(97, 123)])))


print(checkmost("hello"))
print(list(checkall("hello")))
