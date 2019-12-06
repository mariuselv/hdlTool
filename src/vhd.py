"""
========================================================
    Filename: vhd.py
    Author: Marius Elvegård
    Description:


========================================================
"""

_id_keywords = ["ENTITY", "PACKAGE", "CONTEXT"]

class VHD:
    _id_keywords  = ["entity", "package"]

    def __init__(self, filename):
        self.filename        = filename
        self.path            = None
        self.id              = None
        self.dependency_list = []
        self.library         = None
        self.obj_dependency  = []
        self.lib_dependency  = []
            

    # File methods
    def set_filename(self, filename):
        self.filename = filename
    
    def get_filename(self):
        return self.filename

    def set_path(self, path):
        self.path = path

    def get_path(self):
        return self.path

    # Library methods
    def set_library(self, library):
        self.library = library.upper()

    def get_library(self):
        return self.library


    # Object id methods
    def get_id(self):
        return self.id

    def set_id(self, id):
        if type(id) is list:
            if id[0][0].upper() in _id_keywords:
                self.id = id[0][1]
        else:
            self.id = id


    # Dependency methods
    def add_dependency(self, dep_list):
        for dep in dep_list:
            dep_item = dep[1].upper()

            # Library use file
            if "DEPENDENCY_USE" in dep[0].upper():
                dep_item = self._reduce_obj_dependency_item(dep_item)
                self.add_obj_dependency(dep_item)

            # Library
            elif "DEPENDENCY_LIBRARY" in dep[0].upper():
                self.add_lib_dependency(dep_item)

            # Context file
            elif "DEPENDENCY_CONTEXT" in dep[0].upper():
                self.add_obj_dependency(dep_item)

            # Component instantiation in architecture
            elif "DEPENDENCY_ENTITY" in dep[0].upper():
                self.add_obj_dependency(dep_item)


    def add_lib_dependency(self, lib):
        if not(lib.upper() in self.lib_dependency):
            self.lib_dependency.append(lib.upper())

    def add_obj_dependency(self, obj):
        if not(obj.upper() in self.obj_dependency):
            self.obj_dependency.append(obj.upper())

    def _reduce_obj_dependency_item(self, object):
        # Remove everything from final '.', e.g ".all"
        if '.' in object:
            idx = object.rindex('.')
            return_item = object[:idx].lower()
            # Remove everything before first '.', e.g. "work."
            idx = return_item.find('.')
            return_item = return_item[1 + idx:] 
            return return_item
        else:
            return object


    def get_obj_dependency(self):
        return self.obj_dependency
    def get_lib_dependency(self):
        return self.lib_dependency






