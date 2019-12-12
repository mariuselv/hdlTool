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

    def __init__(self, simulator="modelsim"):
        self.compile_directives_vsim = "-quiet -suppress 1346,1236,1090 -2008 -work"
        self.compile_directives_vcom = "-2008 -nowarn COMP96_0564 -nowarn COMP96_0048 -dbg -work"
        self.simulator = simulator

    def _run_cmd(self, cmd, verbose = False):
        if verbose:
            subprocess.call([cmd + ';exit'], stdout=FNULL, stderr=subprocess.PIPE)
        else:
            subprocess.call([cmd + ';exit'], stderr=subprocess.PIPE)

    def compile_file(self, file):
        self._run_cmd("eval vcom " + self.get_compile_directives() + " " + file)

    def compile_files(self, files):
        for file in files:
            self.compile_file(file)


    def set_simulator(self, sim):
        if (sim.lower() == "vsim") or (sim.lower() == "modelsim"):
            self.simulator = "modelsim"
        elif (sim.lower() == "vcom") or (sim.lower() == "riviera"):
            self.simulator = "riviera"
        else:
            self.simulator = sim

    def get_simulator(self):
        return self.simulator


    def set_compile_directives(self, directives):
        if (self.simulator.lower() == "modelsim"):
            self.compile_directives_vsim = directives
        else:
            self.compile_directives_vcom = directives


    def get_compile_directives(self):
        if self.simulator.lower() == "modelsim":
            return self.compile_directives_vsim
        else:
            return self.compile_directives_vcom



