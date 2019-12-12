"""
========================================================
    Filename: hdl_tool.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""

import sys

from finder import Finder
from collection import Collection
from test_suite import Test_suite
from compiler import Compiler


class Hdl_tool():

    def __init__(self):
        self.collection_list = []
        self.organized_list  = []
        self.compiler = Compiler()


    def add_collection(self, collection):
        if not(collection in self.collection_list):
            self.collection_list.append(collection)


    def get_collections(self):
        if self.organize_collection:
            return self.organize_collection
        else:
            return self.collection_list


    def organize_collection(self):
        collection_list_copy = self.collection_list.copy()
        self.organized_list = self.collection_list.copy()

        for run in range(1, len(self.collection_list)):
            for check_collection in collection_list_copy:
                for dep_collection in self.organized_list:
                    if dep_collection.get_library().upper() in check_collection.get_external_dependency():
                        check_idx = self.organized_list.index(check_collection)
                        dep_idx = self.organized_list.index(dep_collection)

                        # Swap items in list
                        if check_idx < dep_idx:
                            self.organized_list[check_idx], self.organized_list[dep_idx] = self.organized_list[dep_idx], self.organized_list[check_idx]


    def list_compile_order(self):
        print("\n================================ HDL Tool ================================")
        for idx, item in enumerate(self.organized_list):
            print("[%i] Lib: %s" %(idx+1, item.get_library()))


    def collection(self):
        return Collection()


    def compile_collection(self):
        if self.organize_collection:
            print(self.organize_collection)
            #for item in self.organize_collection:
             #   print(item)
        else:
            if not(self.collection):
                print("Collection missing")
            elif not(self.organize_collection):
                print("Run organize_collection() first")

    def compile(self):
        self.compile_collection()