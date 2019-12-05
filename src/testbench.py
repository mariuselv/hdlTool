"""
========================================================
    Filename: testbench.py
    Author: Marius Elvegård
    Description:


========================================================
"""

class Testbech:


    def __init__(self):
        self.generics_list = []
        self.filename = None


    def set_filename(self, filename):
        self.filename = filename

    def get_filename(self):
        return self.filename

    
    def add_generic(self, name, value):
        self.generics_list.append([name, value])

    def get_generics(self):
        return self.generics_list