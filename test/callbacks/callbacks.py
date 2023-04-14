# -*- coding: utf-8 -*-
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@mit.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
"""
# from builtins import object

from wield.declarative.callbacks import Callback, callbackmethod

from wield.declarative import (
    OverridableObject,
    mproperty,
    NOARG,
)


oldprint = print
print_test_list = []


def print(*args):
    oldprint(*args)
    if len(args) == 1:
        print_test_list.append(args[0])
    else:
        print_test_list.append(args)


def message(message):
    print(message)


class TCallback(object):
    def __init__(self):
        self.callback = Callback()

    @callbackmethod
    def callbackmethod(self, message):
        print(("callbackmethod", message))


T = TCallback()
T.callback.register(callback=print, key=print)
T.callbackmethod.register(callback=message, key=message)

T.callback("hello")
T.callbackmethod("world")
