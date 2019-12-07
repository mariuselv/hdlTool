"""
========================================================
    Filename: test_suite.py
    Author: Marius Elvegård
    Description: 
      The test suit constist of a test bench, a testharness
      and a set of design files.
      The test suite is used for compiling and running 
      a set of simulations/tests.

    (c) 2019 Marius Elvegård
========================================================
"""

from compiler import Compiler

class Test_suite:

    def __init__(self):
        self.tb_list = []
        self.lib_list = []
        self.testbench = None
        self.compile_order_list = []
        self.compiler = Compiler()

    def add_testbench(self, testbench):
        """
        Set the testbench object for test suite
        """
        self.testbench = testbench

    def get_testbench(self):
        return self.testbench

    
    def set_compile_order(self, compile_order):
        self.compile_order_list = compile_order
    
    def get_compile_order(self):
        return self.compile_order_list

    def compile(self):
        pass

    def simulate(self):
        pass