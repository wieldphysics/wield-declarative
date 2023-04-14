# -*- coding: utf-8 -*-
# SPDX-License-Identifier: CC0-1.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@caltech.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
""" Tests of the argparse api. Not really testing the declarative argparse library, but helpful for development of it.
"""

import argparse

pp = argparse.ArgumentParser(description="HHMMM", add_help=False)
spp = pp.add_subparsers(dest="cmd")
spp1 = spp.add_parser("test", help="HMM")
spp1.add_argument("args", nargs="*", help="holds arguments for other")
spp1 = spp.add_parser("t2", help="cool")
spp1.add_argument("args", nargs=argparse.REMAINDER, help="holds arguments for other")

p = argparse.ArgumentParser(
    description="HHMMM",
    parents=[pp],
)

p.add_argument("-t")

g = p.add_argument_group("system")
g.add_argument("-i", "--ifo", required=True)

g = p.add_argument_group("xyz", "mutually ex").add_mutually_exclusive_group()
g.add_argument("-x")
g.add_argument("-y")
g.add_argument("-z")

p.add_argument(
    "pos",
    default=None,
    choices=["rock", "paper", "scissors"],
    nargs="?",
    help=argparse.SUPPRESS,
)
p.add_argument(
    "args",
    nargs=argparse.REMAINDER,
    help=argparse.SUPPRESS,
)


a = p.parse_args()
print(a)
