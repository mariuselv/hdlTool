"""
========================================================
    Filename: vhd.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""
_dep_keywords = ["LIBRARY", "USE", "CONTEXT", "COMPONENT", "ENTITY"]
_id_keywords = ["ENTITY", "PACKAGE", "CONTEXT"]


class VHD:

    def __init__(self, filename):
        self.filename       = filename
        self.name           = None
        self.path           = None
        self.type           = None
        self.library        = None
        self.lib_dep        = []
        self.use_dep        = []
        self.context_dep    = []

        #self.dependency_list = []
        #self.obj_dependency  = []
        #self.lib_dependency  = []
        
            

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
    def get_type(self):
        return self.type

    def set_type(self, token):
        if type(token) is list:
            if token[0][0].upper() in _id_keywords:
                self.type = token[0][0]
        else:
            self.type = token


    def get_name(self):
        return self.name

    def set_name(self, token):
        if type(token) is list:
            if token[0][0].upper() in _id_keywords:
                self.name = token[0][1]
        else:
            self.name = token


    def _reduce_use_dep_item_string(self, item_str):
        # Remove everything from final '.', e.g ".all"
        if '.' in item_str:
            idx = item_str.rindex('.')
            return_item = item_str[:idx].lower()
            # Remove everything before first '.', e.g. "work."
            idx = return_item.find('.')
            return_item = return_item[1 + idx:] 
            return return_item
        else:
            return item_str


    def add_dependency(self, dep_list):
        for item in dep_list:
            dep_type = item[0]
            dep_id   = item[1]

            if dep_type == "DEPENDENCY_LIBRARY":
                self.lib_dep.append(dep_id)
            elif dep_type == "DEPENDENCY_ENTITY":   # NOTE! Has to be fixed!
                self.use_dep.append(dep_id)
                self.lib_dep.append(dep_id)
            elif dep_type == "DEPENDENCY_CONTEXT":
                self.context_dep.append(dep_id)
            elif dep_type == "DEPENDENCY_USE":
                self.use_dep.append( self._reduce_use_dep_item_string(dep_id) )

    def get_dependencies(self):
        return [self.lib_dep, self.use_dep, self.context_dep]
    def get_use_dep(self):
        return self.use_dep
    def get_lib_dep(self):
        return self.lib_dep
    def get_context_dep(self):
        return self.context_dep



#    # Dependency methods
#    def add_dependency(self, dep_list):
#        for dep in dep_list:
#            dep_item = dep[1].upper()
#
#            # Library use file
#            if "DEPENDENCY_USE" in dep[0].upper():
#                dep_item = self._reduce_obj_dependency_item(dep_item)
#                self.add_obj_dependency(dep_item)
#
#            # Library
#            elif "DEPENDENCY_LIBRARY" in dep[0].upper():
#                self.add_lib_dependency(dep_item)
#
#            # Context file
#            elif "DEPENDENCY_CONTEXT" in dep[0].upper():
#                self.add_obj_dependency(dep_item)
#
#            # Component instantiation in architecture
#            elif "DEPENDENCY_ENTITY" in dep[0].upper():
#                self.add_obj_dependency(dep_item)


#    def add_lib_dependency(self, lib):
#        if not(lib.upper() in self.lib_dependency):
#            self.lib_dependency.append(lib.upper())
#
#    def add_obj_dependency(self, obj):
#        if not(obj.upper() in self.obj_dependency):
#            self.obj_dependency.append(obj.upper())

#    def _reduce_obj_dependency_item(self, object):
#        # Remove everything from final '.', e.g ".all"
#        if '.' in object:
#            idx = object.rindex('.')
#            return_item = object[:idx].lower()
#            # Remove everything before first '.', e.g. "work."
#            idx = return_item.find('.')
#            return_item = return_item[1 + idx:] 
#            return return_item
#        else:
#            return object


#    def get_obj_dependency(self):
#        return self.obj_dependency
#    def get_lib_dependency(self):
#        return self.lib_dependency



