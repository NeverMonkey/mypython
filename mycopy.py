#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# __Author__=neonie

class Point:
    def __int__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r},{self.y!r})'

    # def __repr__(self)
    #     return 'Point(%r,%r)' % (self.x, selfy)
