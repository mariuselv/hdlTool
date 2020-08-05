import sys

sys.path.append('../src')

import pytest
from lexer import Lexer

def setup_function():
    global lexer
    lexer = Lexer("this is the source code")

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
