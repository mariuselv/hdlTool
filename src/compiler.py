"""
========================================================
    Filename: testbench.py
    Author: Marius Elvegård
    Description:
        The compiler is responsible for compiling all 
        items in the test suite, i.e. test bench, 
        testharness and design files.
        The compiler is used by the test suite object.

    (c) 2019 Marius Elvegård
========================================================
"""


class Compiler:


    def __init__(self):
        self.file_list = []


    def add_file_list(self, file_list):
        self.file_list = file_list

