import sys
sys.path.insert(0, 'src')


from finder import Finder
from collection import Collection



def main():

    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()


    collection = Collection()
    collection.set_library("tb_lib")
    collection.add_files(file_list)
    collection.organize()
    collection.list_compile_order()



if __name__ == "__main__":
    main()