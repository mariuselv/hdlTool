import sys
sys.path.insert(0, 'src')


from finder import Finder
from collection import Collection



def main():


    collection_list = []

    # Create a collection and add to list
    print("\nAdding bitvis_vip_uart")
    finder = Finder()
    finder.add_files("test/bitvis_vip_uart/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("bitvis_vip_uart")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)

    print("\nAdding bitvis_vip_sbi")
    finder = Finder()
    finder.add_files("test/bitvis_vip_sbi/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("bitvis_vip_sbi")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)



    print("\nAdding bitvis_vip_scoreboard")
    finder = Finder()
    finder.add_files("test/bitvis_vip_scoreboard/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("bitvis_vip_scoreboard")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)


    print("\nAdding uvvm_util")
    finder = Finder()
    finder.add_files("test/uvvm_util/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("uvvm_util")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)


    print("\nAdding uvvm_vvc_framework")
    finder = Finder()
    finder.add_files("test/uvvm_vvc_framework/src/*.vhd")
    finder.add_files("test/uvvm_vvc_framework/src_target_dependent/*.vhd")
    file_list = finder.get_files()

    collection = Collection()
    collection.set_library("uvvm_vvc_framework")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()

    collection_list.append(collection)



if __name__ == "__main__":
    main()