#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 16:59:03
# @Author  : taihou.nie (nevermonkey@126.com)
# @Link    : https://github.com/NeverMonkey
# @Host    : HP

# Your optional code here
# You can import some modules or create additional functions


def _frequency_filter(n=1):
    return lambda x: x > n


def checkio(data):
    # Your code here
    # It's main function. Don't remove this function
    # It's used for auto-testing and must return a result for check.

    # replace this for solution
    # result = list(filter(_frequency_filter, list(map(data.count, data))))
    data_count = list(map(data.count, data))
    result = [data[i] for i in range(len(data)) if data_count[i] > 1]
    return result

# Some hints
# You can use list.count(element) method for counting.
# Create new list with non-unique elements
# Loop over original list


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [
        10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
