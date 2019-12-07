"""
========================================================
    Filename: finder.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""

import glob



class Finder():


    def __init__(self):
        self.file_list = []

    def add_file(self, filename):
        self.file_list.append(filename)

    def add_files(self, pattern):
        files = glob.glob(pattern)
        for item in files:
            self.add_file(item)

    def get_files(self):
        return self.file_list

    def flush(self):
        self.file_list = []