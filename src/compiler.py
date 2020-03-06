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
import os, sys
import platform

sys.path.insert(0, '../sim')

# Disable terminal output
FNULL = open(os.devnull, 'w')


class Compiler:

    def __init__(self, project_path = ".", simulator="modelsim", filename="compiler.do", testbench=None):
        self.compile_directives_vsim = "-quiet -suppress 1346,1236,1090 -2008 -work"
        self.compile_directives_vcom = "-2008 -nowarn COMP96_0564 -nowarn COMP96_0048 -dbg -work"
        self.simulator               = "modelsim"
        self.library                 = None
        self.project_path            = project_path
        self.compiler_path           = None
        self._compile_file           = None
        self.compile_file_created    = False
        self.compile_file_closed     = False
        self.filename                = filename
        self.testbench               = testbench

    def write(self, str):
        self._compile_file.write(str)

    def _generate_compile_file(self):
        if not(os.path.isdir("sim")):
            os.mkdir("sim")
        filename = self.filename
        print("\nGenerating: sim/%s" %(filename))
        self._compile_file = open("./sim/" + filename, "w");
        self.write("if {[batch_mode]} {\n")
        self.write("  onerror {abort all; exit -f -code 1}\n")
        self.write("} else {\n")
        self.write("  onerror {abort all}\n")
        self.write("}\n\n")
        self.compile_file_created = True
        self.compile_file_closed = False

    def _close_compile_file(self):
        self._compile_file.close()
        self.compile_file_closed = True

    def _add_library_to_compile_file(self, lib):
        self.write("\nvlib " + lib + "\n")
        self.write("vmap " + lib + " " + lib + "\n")

    def add_to_compile_file(self, file):
        self.write("eval vcom " + self.get_compile_directives() + " " + self.get_library() + "  ../" + file + "\n")

    def _get_project_path(self):
        return self.project_path

    def _os_is_win(self):
        return 'windows' in platform.system().lower()


    def compile_file(self, file):
        """
        Compile VHD files
        """  
        if not(self.compile_file_created): 
            self._generate_compile_file()
            self._add_library_to_compile_file(self.get_library())

        file = '/'.join(file.split('\\'))      
        self.add_to_compile_file(file)


    def compile_files(self, vhdl_collection):
        """
        Compile VHD file objects
        """
        for vhd_obj in vhdl_collection:
            filename = vhd_obj.get_filename()
            self.compile_file(filename)


    def run_compilation(self):
        if not(self.compile_file_closed): self._close_compile_file()

        path = os.getcwd().replace("\\", "/") + "/sim"

        self.env_var = os.environ.copy()
        self.env_var["SIMULATOR"] = "MODELSIM"
        print("Compiler compiling : %s" %(self.filename))
        process = subprocess.Popen(['vsim', '-c', '-do', 'do ' + self.filename + '; exit -f'], env=self.env_var, stderr=subprocess.PIPE, cwd=path)
        process.wait()

    def set_simulator(self, sim):
        if (sim.lower() == "vsim") or (sim.lower() == "modelsim"):
            self.simulator = "modelsim"
        elif (sim.lower() == "vcom") or (sim.lower() == "riviera"):
            self.simulator = "riviera"
        else:
            self.simulator = "modelsim"

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
        if self._compile_file:
            self._add_library_to_compile_file(library)
        self.library = library

    def get_library(self):
        if not self.library:
            print("WARNING! Library not set")
        return self.library

    def clean_up(self):
        if not(self.compile_file_closed): self._close_compile_file()
