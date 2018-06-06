#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 18:00:15
# @Author  : taihou.nie (nevermonkey@126.com)
# @Link    : https://github.com/NeverMonkey
# @Host    : HP


def count_words(text, words):
    word_count = list(map(text.lower().count, words))
    count_result = 0
    for i in word_count:
        if i >= 1:
            count_result = count_result + 1
    return(count_result)

# def count_words(text, words):
#     count = 0
#     for i in words:
#         if (text.lower().find(i)) >= 0:
#             count += 1
#     return(count)

# return sum(w in text.lower() for w in words)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {
                       "how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {
                       "banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
