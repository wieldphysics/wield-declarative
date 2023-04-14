# -*- coding: utf-8 -*-
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@caltech.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
Test of the argparse library

TODO: use automated features
"""


from declarative import (
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


class OOT(OverridableObject):
    """
    Runs the argparse test setup
    """

    @mproperty
    def A(self, val=NOARG):
        if val is NOARG:
            val = "A"
        print(val)
        return val

    @mproperty
    def B(self, val=NOARG):
        if val is NOARG:
            val = "B"
        print(val)
        return val


def test_mproperty():
    print_test_list[:] = []
    test = OOT()
    assert print_test_list == []

    print_test_list[:] = []
    test = OOT()
    test.A
    assert print_test_list == ["A"]

    print_test_list[:] = []
    test = OOT(B="BB")
    test.A
    test.B
    assert print_test_list == ["A", "BB"]


class TBadAccess(OverridableObject):
    """
    Runs the argparse test setup
    """

    @mproperty
    def no_args(self):
        print("A")
        return "A"

    @mproperty
    def bad_set(self):
        None.Test
        return "B"


if __name__ == "__main__":
    test_mproperty
