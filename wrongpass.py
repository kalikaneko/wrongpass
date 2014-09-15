#!/bin/env python
# -*- coding: utf-8 -*-
# wrongpass.py
# Copyright (C) 2014 Kali Kaneko
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
A bloom filter with the 10k worst passwords.
"""
import os
from pybloom import BloomFilter

_BLOOM_DUMP = "worst.bloom"
_WORST_DUMP = "data/10kworst.txt"

_bloom = None


def _build_filter():
    bf = BloomFilter(capacity=10000, error_rate=0.001)
    worst = [w[:-2] for w in open(_WORST_DUMP).readlines()]
    map(bf.add, worst)
    with open(_BLOOM_DUMP, 'w') as f:
        bf.tofile(f)
    print "Serialized bloom filter to ", _BLOOM_DUMP


def _load_filter():
    bf = BloomFilter.fromfile(open(_BLOOM_DUMP))
    return bf


def I_can_has(wrongpassword):
    wrongpassword = unicode(wrongpassword)
    global bloom
    if _bloom is None:
        bloom = _load_filter()
    return wrongpassword not in bloom


def test_values(testset=None):
    print "Loading filter..."
    bf = _load_filter()

    if testset is None:
        testset = {"1234", "mygod", "theboss", "veryhardpass", "asdasd",
                   "password", "fucker"}
    for w in testset:
        print w, "in filter? ", w in bf


if __name__ == "__main__":
    import sys
    if sys.argv[1] == "build":
        if not os.path.isfile(_BLOOM_DUMP):
            "Building filter..."
            _build_filter()
    if sys.argv[1] == "test":
        test_values()


__all__ = [I_can_has]
