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
        self.tb_list                    = []
        self.lib_list                   = []
        self.testbench                  = None
        self.compiler                   = Compiler()
        self.organize_collection_list   = []


    def add_testbench(self, testbench):
        """
        Set the testbench object for test suite.
        Args:
          testbench (str): testbench filename and path
        """
        self.testbench = testbench

    def get_testbench(self):
        return self.testbench


    def set_collection(self, organize_collection_list):
        """
        Add a collection to test suite

        Args:
          organize_collection_list (Collection object): a collection of VHDL object files.
        """
        self.organize_collection_list = organize_collection_list

    def get_collection(self):
        return self.organize_collection_list


    def compile(self):
        #self.compiler.compile(self.organize_collection_list)
        pass


    def simulate(self):
        pass
