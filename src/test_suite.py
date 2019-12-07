"""
========================================================
    Filename: test_suite.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""


class Test_suite:

    def __init__(self):
        self.tb_list = []
        self.lib_list = []
        self.testbench = None
        self.compile_order_list = []

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