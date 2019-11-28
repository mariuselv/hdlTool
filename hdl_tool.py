import sys



sys.path.insert(0, 'dep')
from parser import Parser
from lexer import Lexer
from finder import Finder
from vhd import VHD


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

        vhd_object.add_dependency(dep_list)        
        
        print("OBJ: %s" %(vhd_object.get_obj_dependency()))
        print("LIB: %s" %(vhd_object.get_lib_dependency()))

        vhd_files.append(vhd_object)


def main():
    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()

    colonize(file_list)




if __name__ == "__main__":
    main()