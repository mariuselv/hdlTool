"""
========================================================
    Filename: collection.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""

from pars import Parser
from lexer import Lexer
from vhd import VHD
from glob import glob
import os



class Collection:


    def __init__(self):
        self.vhdl_obj_list = []
        self.vhdl_source_file_list = []
        self.library = None
        self.finder = Finder()


    def set_library(self, library) -> None :
        """ Set the compile library. """
        self.library = library

    def get_library(self) -> str : 
        return self.library


    def add_file(self, vhdl_file) -> bool :
        """ Adds a single file to builder. """
        if not os.path.isfile(vhdl_file): return False

        if not vhdl_file in self.vhdl_source_file_list:
            self.vhdl_source_file_list.append(vhdl_file)
            return True
        return False


    def add_files(self, vhdl_files) -> bool :
        """
        Adds a list of files to builder.
        """
        return_result = True
        self.finder.add_files(vhdl_files)

        for vhdl_file in self.finder.get_files():
            if not(self.add_file(vhdl_file)):
                return_result = False
        return return_result


    def _swap(self, list, i, j) -> list:
        list[i], list[j] = list[j], list[i]
        return list


    def _sort_compile_order(self, vhdl_file_list) -> list :
        sorted_list = vhdl_file_list.copy()

        # Slow sorting method, need N-1 loops
        for sort_loop in range(1, len(sorted_list)-1):

            # Pick item to check in dependency lists
            for sort_item in vhdl_file_list:
                sort_name = sort_item.get_name()

                # Pick item which dependency list should be checked
                for check_item in sorted_list:
                    lib_dep, use_dep, context_dep = check_item.get_dependencies()

                    # Is sort_item in check_item's dependency list?
                    if sort_name in use_dep:

                        # Should items be swapped based on index in sorted_list?
                        sort_idx = sorted_list.index(sort_item)
                        check_idx = sorted_list.index(check_item)
                        if check_idx < sort_idx:
                            sorted_list = self._swap(sorted_list, sort_idx, check_idx)

        self.vhdl_obj_list = sorted_list


    def organize_collection(self):
        """
        With all files in collection do:
        1. Create a vhdl_object() object
        2. Tokenize file
        3. Parse file
        4. Read file dependencies
        5. Read type of file
        6. Set vhdl_object name, type and dependencies.
        7. Add vhdl_object to vhdl_object_list
        8. Detect vhdl_object generics

        -> Final, sort vhdl_objects by dependency.
        """

        for file_item in self.vhdl_source_file_list:
            # Get new VHDL object
            vhdl_object = VHD(file_item)

            # Read file content
            with open(file_item, 'r') as file:
                content = file.read()

            # Lexer
            lex = Lexer(content)
            tokens = lex.tokenize()

            # Parser
            parser      = Parser(tokens)
            # Get the vhdl objects dependencies
            dep_list    = parser.get_dependency()
            # Get the type of vhdl object
            vhdl_type    = parser.get_type()

            # VHDL object
            # Set the name of vhdl object
            vhdl_object.set_name(vhdl_type)
            # Set the type of vhdl object
            vhdl_object.set_type(vhdl_type)
            # Set the vhdl object dependencies
            vhdl_object.add_dependency(dep_list)

            # Add vhdl object to list
            self.vhdl_obj_list.append(vhdl_object)

            vhdl_object.get_generics(tokens)

        # Organize VHDL objects by internal dependeny
        self._sort_compile_order(self.vhdl_obj_list)


    def get_compile_order(self) -> list :
        """ Return list of library internal dependencies. """
        return self.vhdl_obj_list


    def get_external_dependency(self) -> list :
        """ Return list of external libraries dependencies. """
        ret_list = []
        for obj in self.vhdl_obj_list:
            libs = obj.get_lib_dep()
            for lib in libs:
                if not lib in ret_list:
                    ret_list.append(lib)

        return ret_list


    def list_compile_order(self) -> None :
        print("\n================================ %s ================================" %(self.get_library()))
        for idx, item in enumerate(self.vhdl_obj_list):
            print("[%i] File: %s (%s: %s)" %(idx+1, item.get_filename(), item.get_type(), item.get_name()))







class Finder():
    """
    Use for file search and adding files.
    """

    def __init__(self):
        self.file_list = []

    def add_file(self, filename) -> None :
        if not filename in self.file_list:
            self.file_list.append(filename)

    def add_files(self, pattern) -> None:
        files = glob(pattern)
        for item in files:
            self.add_file(item)

    def get_files(self) -> list :
        return self.file_list

    def flush(self) -> None :
        self.file_list = []