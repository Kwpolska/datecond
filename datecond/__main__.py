#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Date Conditionals (datecond)
# Version 0.1.2
# Copyright © 2015-2016, Chris Warrick.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions, and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions, and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# 3. Neither the name of the author of this software nor the names of
#    contributors to this software may be used to endorse or promote
#    products derived from this software without specific prior written
#    consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Main demo function for datecond."""

from __future__ import print_function, unicode_literals
from datecond import date_in_range
import dateutil.parser

try:
    inpf = raw_input
except NameError:
    inpf = input


def main():
    """Run main demo function."""
    date_range = inpf("Date range to accept: ")
    while True:
        test_str = inpf("Date to test: ")
        test_date = dateutil.parser.parse(test_str)
        print("    Date parsed:", test_date)
        print("    In range:", date_in_range(date_range, test_date, True))

if __name__ == '__main__':
    main()
