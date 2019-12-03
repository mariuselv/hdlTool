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
    ordered_list = object_list.copy()
    compare_list = object_list.copy()

    # Need N-1 runs to get complete ordered list
    for run in range(1, len(object_list)):

        # Object which dependency list will be checked
        for check_item in compare_list:

            # Object which will be checked if is in dependency list
            for dep_item in ordered_list:

                # check_item has dependency on dep_item    
                if dep_item[0].get_id().upper() in check_item[0].get_obj_dependency():
                
                    # Get objcts indexes from list
                    check_item_idx = ordered_list.index(check_item)
                    dep_item_idx = ordered_list.index(dep_item)

                    # check if index of dependent object is higher and swap if so
                    if check_item_idx < dep_item_idx:
                        #print("Swapping:  %s   <<---->>   %s" %(check_item[0].get_id(), dep_item[0].get_id()))
                        ordered_list[check_item_idx], ordered_list[dep_item_idx] = ordered_list[dep_item_idx], ordered_list[check_item_idx]

        # Update list for next run
        compare_list = ordered_list.copy()

    # Return the ordered list
    return ordered_list





def organize_dependencies(object_list):
    organized_dependencies_list = []

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

            # Same file or undefined (e.g. context file), skip this one
            if is_match(seek_file, item_file) or (seek_name is None):
                continue

            # Organize dependencies
            if seek_name.upper() in item_obj_dep:
                local_dependencies.append(seek_item)
            else:
                external_dependencies.append(seek_item)

        # Add VHD object with its local_depdendencies list and external_dependencies list
        organized_dependencies_list.append([item, local_dependencies, external_dependencies])

    # Return list with all VHD objectes and their local_dependencies and external_dependencies lists
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
        vhd_files.append(vhd_object)



    # Check list
    organized_dependencies_list = organize_dependencies(vhd_files)

    # Organize compile order
    compile_list = reorder_dependencies(organized_dependencies_list)

    print("Compile order:")
    for idx, item in enumerate(compile_list):
        print("[%i] %s: %s" %(idx, item[0].get_filename(), item[0].get_id()))


def main():
    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()

    colonize(file_list)




if __name__ == "__main__":
    main()