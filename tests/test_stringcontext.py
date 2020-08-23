#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_stringcontext
----------------------------------
Tests for `stringcontext` module.
"""

import stringcontext

s = "Hello World test"
index = 5
contextnum = 5


def test_context_after():
    c = stringcontext.context_after(s, index, contextnum)
    assert c == "World"


def test_context_before():
    c = stringcontext.context_before(s, index, contextnum)
    assert c == "Hello"


def test_context_before_gt_len():
    c = stringcontext.context_before(s, index, 7)
    assert c == "Hello"


def test_context():
    c = stringcontext.context(s, index, contextnum)
    assert c == "Hello World"


def test_context_emptystr():
    c = stringcontext.context('', index, contextnum)
    assert c == ''
    c = stringcontext.context('', 0, 0)
    assert c == ''
