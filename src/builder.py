from parser import Parser
from lexer import Lexer
from vhd import VHD



class Builder:


    def __init__(self):
        self.vhd_files = []
        self.vhd_file_list = []
        self.organized_dependencies_list = []
        self.library = None



    def set_library(self, library):
        """
        Set the compile library.
        """
        self.library = library

    def get_library(self):
        return self.library


    def add_files(self, files):
        """
        Adds a list of files to builder.
        """
        for item in files:
            if not(item in self.vhd_file_list):
                self.vhd_file_list.append(item)

    def add_file(self, file):
        """
        Adds a single file to builder.
        """
        if not file in self.vhd_file_list:
            self.vhd_file_list.append(file)


    def _is_match(self, item1, item2):
        """
        Internal method for comparing two strings.
        """
        if item1.upper() == item2.upper():
            return True
        else:
            return False


    def _add_external_dependencies(self, object_list):
        print(len(object_list[2]))
        for item in object_list[1]:
            print(item.get_id())


    def reorder_dependencies(self, object_list):
        """
        Updates the ordere_list with VHD items in correct 
        compile order.
        """
        self._add_external_dependencies(object_list[2])

        self.ordered_list = object_list.copy()
        compare_list = object_list.copy()

        # Need N-1 runs to get complete ordered list
        for run in range(1, len(object_list)):

            # Object which dependency list will be checked
            for check_item in compare_list:

                # Object which will be checked if is in dependency list
                for dep_item in self.ordered_list:

                    # check_item has dependency on dep_item    
                    if dep_item[0].get_id().upper() in check_item[0].get_obj_dependency():
                    
                        # Get objcts indexes from list
                        check_item_idx = self.ordered_list.index(check_item)
                        dep_item_idx = self.ordered_list.index(dep_item)

                        # check if index of dependent object is higher and swap if so
                        if check_item_idx < dep_item_idx:
                            self.ordered_list[check_item_idx], self.ordered_list[dep_item_idx] = self.ordered_list[dep_item_idx], self.ordered_list[check_item_idx]

            # Update list for next run
            compare_list = self.ordered_list.copy()




    def organize_dependencies(self, object_list):
        """
        Updates the organized_dependencies_list with all VHD objectes and 
        their local_dependencies and external_dependencies lists.
        """

        # Loop all VHD files in object_list
        for item in object_list:
            item_name    = item.get_id()
            item_file    = item.get_filename()
            #item_lib_dep = item.get_lib_dependency()
            item_obj_dep = item.get_obj_dependency()

            local_dependencies = []
            external_dependencies = []

            # Skip non-defined objects (context etc)
            if item_name is None:
                continue

            # Loop all VHD files in object list and check if any
            #   is present in the item_obj_dep list. If so, add
            #   VHD object to local_dependencies list, else add it
            #   to externatl_dependencies list.
            for seek_item in object_list:
                seek_name = seek_item.get_id()
                seek_file = seek_item.get_filename()

                # Same file or undefined, skip this one
                if self._is_match(seek_file, item_file) or (seek_name is None):
                    continue

                # Organize dependencies
                if seek_name.upper() in item_obj_dep:
                    local_dependencies.append(seek_item)
                else:
                    external_dependencies.append(seek_item)

            # Add VHD object with its local_depdendencies list and external_dependencies list
            self.organized_dependencies_list.append([item, local_dependencies, external_dependencies])




    def colonize(self):    
        tokens = []

        for file_item in self.vhd_file_list:

            vhd_object = VHD(file_item)

            with open(file_item, 'r') as file:
                content = file.read() 

            # Lexer
            lex = Lexer(content)
            tokens = lex.tokenize()

            # Parser
            parser      = Parser(tokens)
            # Get the VHD objects dependencies
            dep_list    = parser.get_dependency()
            # Get the type of VHD object
            vhd_type    = parser.get_type()

            # VHD object
            # Set the type of VHD object
            vhd_object.set_id(vhd_type)
            # Set the VHD object dependencies
            vhd_object.add_dependency(dep_list)        

            # Add VHD object to list
            self.vhd_files.append(vhd_object)


        # Check list
        self.organize_dependencies(self.vhd_files)

        # Organize compile order
        self.reorder_dependencies(self.organized_dependencies_list)





    def list_compile_order(self):
        print("Compile order:")
        for idx, item in enumerate(self.ordered_list):
            print("[%i] %s: %s" %(idx, item[0].get_filename(), item[0].get_id()))
