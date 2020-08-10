import sys

sys.path.append('../src')

import pytest
from lexer import Lexer

def setup_function():
    global lexer
    lexer = Lexer("this is the source code\nthis is the second line\nthis is the third line\n")

def tear_down_function():
    pass


def test_complete_string_double_quote():
    result = lexer._complete_string('"this is a complete string"', '\"')
    assert result == True, "Expecting complete double quoted string"

def test_complete_string_single_quote():
    result = lexer._complete_string('"this is a complete string"', "\'")
    assert result == True, "Expecting complete single quoted string"

def test_incomplete_string_double_quote():
    result = lexer._complete_string('"this is an incomplete string', '\"')
    assert result == False, "Expecting incomplete double quoted string"

def test_incomplete_string_single_quote():
    result = lexer._complete_string("'this is an incomplete string", "\'")
    assert result == False, "Expecting incomplete single quoted string"

def test_word_counters():
    result = lexer.get_tokens()

    assert result[0][2] == 1, "Expecting line 1"
    assert result[0][3] == 1, "Expecting word 1"

    assert result[1][2] == 1, "Expecting line 1"
    assert result[1][3] == 2, "Expecting word 2"

    assert result[4][2] == 1, "Expecting line 1"
    assert result[4][3] == 5, "Expecting word 5"

    assert result[5][2] == 1, "Expecting line 1"
    assert result[5][3] == 6, "Expecting word 6"

    assert result[6][2] == 2, "Expecting line 2"
    assert result[6][3] == 1, "Expecting word 1"