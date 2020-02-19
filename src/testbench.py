"""
========================================================
    Filename: testbench.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""

import subprocess, os
from compiler import Compiler


class Testbench:

    def __init__(self, testbench_name, project_path=".", simulator="modelsim", verbose=False):
        self.generics_list      = []
        self.filename           = None
        self.testbench_name     = testbench_name
        self.entity             = None
        self.library            = None
        self.simulator          = simulator
        self.verbose            = verbose
        self.compiler           = Compiler(project_path, filename="tb_compiler.do")

    def get_testbench_name(self):
        return self.testbench_name
    def set_testbench_name(self, name):
        self.testbench_name = name

    def set_entity(self, name):
        self.entity = name
    def set_name(self, name):
        self.entity(name)

    def get_entity(self):
        return self.entity
    def get_name(self):
        return self.get_entity()

    def set_library(self, library):
        self.library = library.lower()
    def get_library(self):
        return self.library

    def set_filename(self, filename):
        self.filename = filename
    def get_filename(self):
        return self.filename

    def set_harness(self, harness):
        self.harness = harness
    def get_harness(self):
        return self.harness

    def add_generic(self, name, value):
        self.generics_list.append([name, value.lower()])
    def add_generics(self, generics_list):
        for name, value in generics_list:
            self.add_generic(name, value)
    def get_generics(self):
        return self._get_generics()


    def _get_generics(self):
        generic_list = []
        for generic in self.generics_list:
            generic_list.append("-g" + generic[0].upper() + "=" + generic[1].lower() + " ")
        return generic_list

    def _run_cmd(self, cmd, path="."):
        print("Running: %s" %(cmd))
        if self.verbose:
            run = subprocess.run(cmd, cwd=path, stdout=FNULL, stderr=subprocess.PIPE, shell=True, env={'PATH': os.getenv('PATH')})
        else:
            run = subprocess.run(cmd, cwd=path, stderr=subprocess.PIPE, shell=True, env={'PATH': os.getenv('PATH')})

    def set_compile_directives(self, directives, simulator="modelsim"):
        self.compile_directives = directives

    def _set_compile_directices(self, simulator="modelsim"):
        if simulator.lower() == "aldec" or simulator.lower() == "rivierapro":
            self.compile_directives = "-2008 -nowarn COMP96_0564 -nowarn COMP96_0048 -dbg -work " + self.get_library()
        else:
            self.compile_directives = "-suppress 1346,1236 -2008 -work " + self.get_library()

    def get_compile_directives(self, simulator="modelsim"):
        if simulator.lower() == "aldec" or simulator.lower() == "rivierapro":
            return "-2008 -nowarn COMP96_0564 -nowarn COMP96_0048 -dbg -work " + self.get_library()
        else:
            return "-suppress 1346,1236 -2008 -work " + self.get_library()

    def run_testbench(self, simulator="modelsim"):
        if self.compiler:
            self.compiler.set_library(self.get_library())
            self.compiler.compile_file(self.get_harness())
            self.compiler.add_to_compile_file(self.get_testbench_name())
            self.compiler.set_testbench(self.get_entity())
        else:
            print("ERROR! No compile file created")

        self.compiler.add_generics_to_compile_file(self._get_generics())
        self.compiler.run_simulation()

