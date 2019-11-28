import sys



sys.path.insert(0, 'dep')
from parser import Parser
from lexer import Lexer
from finder import Finder
from vhd import VHD


def is_match(item1, item2):
    if item1.upper() == item2.upper():
        return True
    else:
        return False



def reorder_dependencies(object_list):
    ordered_list = []



    return ordered_list




def organize_dependencies(object_list):

    organized_dependencies_list = []
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
        
        for seek_item in object_list:
            seek_name = seek_item.get_id()
            seek_file = seek_item.get_filename()

            # Same file or undefined (e.g. context file), skip this one
            if is_match(seek_file, item_file) or (seek_name is None):
                continue

            # Organize dependencies
            if seek_name.upper() in item_obj_dep:
                local_dependencies.append(seek_item)
            else:
                external_dependencies.append(seek_item)

        organized_dependencies_list.append([item, local_dependencies, external_dependencies])

    return organized_dependencies_list





def colonize(file_list):    
    tokens = []
    vhd_files = []

    for file_item in file_list:

        vhd_object = VHD(file_item)

        with open(file_item, 'r') as file:
            content = file.read() 
    
        # Lexer
        lex = Lexer(content)
        tokens = lex.tokenize()
    
        # Parser
        parser      = Parser(tokens)
        dep_list    = parser.get_dependency()
        vhd_type    = parser.get_type()

        # VHD object
        vhd_object.add_dependency(dep_list)        
        vhd_object.set_id(vhd_type)

        # Add to list
        vhd_files.append(vhd_object)

    # Check list
    organized_dependencies_list = organize_dependencies(vhd_files)





def main():
    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()

    colonize(file_list)




if __name__ == "__main__":
    main()