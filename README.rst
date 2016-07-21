============================
Date Conditionals (datecond)
============================
:Info: This is the README file for Date Conditionals.
:Author: Chris Warrick <chris@chriswarrick.com>
:Copyright: © 2016, Chris Warrick.
:Date: 2016-07-21
:Version: 0.1.4

.. index: README
.. image:: https://travis-ci.org/Kwpolska/datecond.svg?branch=master
   :target: https://travis-ci.org/Kwpolska/datecond

PURPOSE
-------

This is a minimalistic (and slightly hacky) parser for date range conditionals.

INSTALLATION
------------

::

  pip install datecond

FORMAT
------

* comma-separated clauses (AND)
* clause: attribute comparison_operator value (spaces optional)
    * attribute: year, month, day, hour, month, second, weekday, isoweekday or empty for full datetime
    * comparison_operator: == != <= >= < >
    * value: integer or dateutil-compatible date input

API
---

The library exposes only one function:

::

   date_in_range(date_range, date, debug=True)

Where ``date_range`` is the date conditional (see `FORMAT`_ above), and
``date`` is a datetime object.

CLI USAGE
---------

::

    $ python -m datecond
    Date range to accept: year == 2016
    Date to test: 2016-01-01
        Date parsed: 2016-01-01 00:00:00
        <2016 == 2016>
        In range: True
    Date to test: 2016-02-02
        Date parsed: 2016-02-02 00:00:00
        <2016 == 2016>
        In range: True
    Date to test: 2017-01-01
        Date parsed: 2017-01-01 00:00:00
        <2017 == 2016>
        In range: False

    $ python -m datecond
    Date range to accept: year == 2016, month > 06, day >= 07
    Date to test: 2016-06-07
        Date parsed: 2016-06-07 00:00:00
        <2016 == 2016>
        <6 > 6>
        <7 >= 7>
        In range: False
    Date to test: 2016-07-07
        Date parsed: 2016-07-07 00:00:00
        <2016 == 2016>
        <7 > 6>
        <7 >= 7>
        In range: True
    Date to test: 2016-08-08
        Date parsed: 2016-08-08 00:00:00
        <2016 == 2016>
        <8 > 6>
        <8 >= 7>
        In range: True
    Date to test: 2015-07-07
        Date parsed: 2015-07-07 00:00:00
        <2015 == 2016>
        <7 > 6>
        <7 >= 7>
        In range: False

COPYRIGHT
---------

Copyright © 2015-2016, Chris Warrick.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions, and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions, and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

3. Neither the name of the author of this software nor the names of
   contributors to this software may be used to endorse or promote
   products derived from this software without specific prior written
   consent.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
