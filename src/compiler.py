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
import platform


# Disable terminal output
FNULL = open(os.devnull, 'w')


class Compiler:

    def __init__(self, project_path = ".", simulator="modelsim"):
        self.compile_directives_vsim = "-quiet -suppress 1346,1236,1090 -2008 -work"
        self.compile_directives_vcom = "-2008 -nowarn COMP96_0564 -nowarn COMP96_0048 -dbg -work"
        self.simulator = simulator
        self.project_path = project_path


    def _get_project_path(self):
        return self.project_path


    def _get_compile_path(self):
        path = (self._get_project_path() + "/sim/")
        if self._os_is_win():
            path = '/'.join(path.split('\\'))
        return path


    def _os_is_win(self):
        return 'windows' in platform.system().lower()


    def _run_cmd(self, cmd, verbose = False):
        path = self._get_compile_path()
        if verbose:
            subprocess.check_call(cmd, stdout=FNULL, stderr=subprocess.PIPE, shell=True)
        else:
            subprocess.check_call(cmd, stderr=subprocess.PIPE, shell=True)


    def _set_lib(self):
        path = self._get_compile_path()
        if not(os.path.isdir(path)):
            os.mkdir(path)

        if not(os.path.isdir("./sim/" + self.get_library())):
            self._run_cmd([path + "vlib", self.get_library()])

        self._run_cmd([path + "vmap", self.get_library(), "./" + self.get_library()])


    def compile_file(self, file):
        self._set_lib()
        if self._os_is_win():
            file = '/'.join(file.split('\\'))
        self._run_cmd(["vcom", self.get_compile_directives(), self.get_library(), file])


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


    def set_library(self, library):
        self.library = library


    def get_library(self):
        return self.library



