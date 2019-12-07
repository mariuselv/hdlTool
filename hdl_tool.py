import sys
sys.path.insert(0, 'src')


from finder import Finder
from collection import Collection


def organize(collection_list):
    collection_list_copy = collection_list.copy()
    return_list = collection_list.copy()

    for run in range(1, len(collection_list)):
        for check_collection in collection_list_copy:
            for dep_collection in return_list:
                if dep_collection.get_library().upper() in check_collection.get_external_dependency():
                    check_idx = return_list.index(check_collection)
                    dep_idx = return_list.index(dep_collection)

                    if check_idx < dep_idx:
                        return_list[check_idx], return_list[dep_idx] = return_list[dep_idx], return_list[check_idx]

    return return_list




def main():

    finder = Finder()

    collection_list = []



    # Create a collection and add to list
    finder.add_files("test/bitvis_vip_uart/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("bitvis_vip_uart")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)

    finder.flush()
    finder.add_files("test/bitvis_vip_sbi/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("bitvis_vip_sbi")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)

    finder.flush()
    finder.add_files("test/bitvis_vip_scoreboard/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("bitvis_vip_scoreboard")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)

    finder.flush()
    finder.add_files("test/uvvm_util/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("uvvm_util")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)

    finder.flush()
    finder.add_files("test/uvvm_vvc_framework/src/*.vhd")
    finder.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("uvvm_vvc_framework")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)


    # Organize how libs has to be compiled
    organize_collection_list = organize(collection_list)
    print("\nLibraries compile order:")
    for item in organize_collection_list:
        print(item.get_library())


if __name__ == "__main__":
    main()