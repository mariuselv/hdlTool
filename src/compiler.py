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

import subprocess
import os

# Disable terminal output
FNULL = open(os.devnull, 'w')


class Compiler:


    def __init__(self):
        self.file_list = []
        self.compile_directives_vsim = "-quiet -suppress 1346,1236,1090 -2008 -work"
        self.compile_directives_vcom = "-2008 -nowarn COMP96_0564 -nowarn COMP96_0048 -dbg -work"
        self.simulator = "vsim"


    def add_file_list(self, file_list):
        self.file_list = file_list


    def _run_cmd(self, cmd, verbose = False):
        if verbose:
            subprocess.call([cmd + ';exit'], stdout=FNULL, stderr=subprocess.PIPE)
        else:
            subprocess.call([cmd + ';exit'], stderr=subprocess.PIPE)


    def set_compile_directives(self, directives):
        if self.simulator is "vsim":
            self.compile_directives_vsim = directives
        else:
            self.compile_directives_vcom = directives

    def add_compile_directives(self, directives):
        if self.simulator is "vsim":
            self.compile_directives_vsim += " " + directives
        else:
            self.compile_directives_vcom += " " + directives

    def get_compile_directives(self):
        if self.simulator is "vsim":
            return self.compile_directives_vsim
        else:
            return self.compile_directives_vcom


    def set_simulator(self, simulator):
        self.simulator = simulator

    def get_simulator(self):
        return self.simulator


    def compile(self, organize_collection_list):
        pass