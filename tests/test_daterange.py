#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# datecond test suite
# Copyright © 2016-2017, Chris Warrick.
# See /LICENSE for licensing information.


from datecond import date_in_range
from datetime import datetime

def test_single_cond_eq():
    pattern = "year == 2016"
    assert date_in_range(pattern, datetime(2016, 1, 1))
    assert date_in_range(pattern, datetime(2016, 12, 31))
    assert date_in_range(pattern, datetime(2016, 7, 13))
    assert not date_in_range(pattern, datetime(2015, 1, 1))
    assert not date_in_range(pattern, datetime(2015, 5, 5))


def test_single_cond_neq():
    pattern = "day != 1"
    assert date_in_range(pattern, datetime(2016, 1, 2))
    assert date_in_range(pattern, datetime(2015, 1, 2))
    assert date_in_range(pattern, datetime(2016, 12, 31))
    assert not date_in_range(pattern, datetime(2015, 1, 1))
    assert not date_in_range(pattern, datetime(2015, 12, 1))


def test_single_cond_gt():
    pattern = "month > 6"
    assert not date_in_range(pattern, datetime(2000, 6, 1))
    assert date_in_range(pattern, datetime(2000, 7, 1))
    assert date_in_range(pattern, datetime(2016, 8, 31))
    assert not date_in_range(pattern, datetime(2006, 1, 6))


def test_multiple_cond():
    pattern = "year == 2016, month > 6, day != 1"
    assert date_in_range(pattern, datetime(2016, 7, 2))
    assert date_in_range(pattern, datetime(2016, 12, 31))
    assert not date_in_range(pattern, datetime(2015, 7, 2))
    assert not date_in_range(pattern, datetime(2016, 6, 2))
    assert not date_in_range(pattern, datetime(2016, 7, 1))
    assert not date_in_range(pattern, datetime(2015, 6, 1))


def test_exact_date():
    pattern = "<= 2016-07-13"
    assert date_in_range(pattern, datetime(2016, 7, 13))
    assert date_in_range(pattern, datetime(2016, 7, 12))
    assert not date_in_range(pattern, datetime(2016, 7, 14))
    assert not date_in_range(pattern, datetime(2016, 8, 13))
    assert date_in_range(pattern, datetime(2010, 1, 1))
    assert not date_in_range(pattern, datetime(2017, 1, 1))


def test_weekday_isoweekday():
    pattern = "weekday == 2"
    assert date_in_range(pattern, datetime(2016, 7, 13))
    assert not date_in_range(pattern, datetime(2016, 7, 14))
    pattern = "weekday != 0"
    assert date_in_range(pattern, datetime(2016, 7, 13))
    assert not date_in_range(pattern, datetime(2016, 7, 11))
    pattern = "isoweekday == 3"
    assert date_in_range(pattern, datetime(2016, 7, 13))
    assert not date_in_range(pattern, datetime(2016, 7, 14))
    pattern = "isoweekday != 1"
    assert date_in_range(pattern, datetime(2016, 7, 13))
    assert not date_in_range(pattern, datetime(2016, 7, 11))


def test_now():
    pattern = "< now"
    assert date_in_range(pattern, datetime(2016, 7, 13), now=datetime(2016, 7, 14))
    assert not date_in_range(pattern, datetime(2016, 7, 14), now=datetime(2016, 7, 14))
