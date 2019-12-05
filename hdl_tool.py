import sys
sys.path.insert(0, 'src')


from finder import Finder
from builder import Builder



def main():

    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()


    builder = Builder()
    builder.add_files(file_list)
    builder.colonize()
    builder.list_compile_order()



if __name__ == "__main__":
    main()