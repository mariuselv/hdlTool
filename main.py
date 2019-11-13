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

        vhd_file = VHD(file_item)

        with open(file_item, 'r') as file:
            content = file.read() 
    
        # Lexer
        lex = Lexer(content)
        tokens = lex.tokenize()
    
        # Parser
        parser = Parser(tokens)
        dependency = parser.get_dependency()
        entity = parser.get_entity()

        # Save file item
        vhd_file.set_dependency(dependency)
        vhd_file.set_entity(entity)

        vhd_files.append(vhd_file)





def main():
    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()

    colonize(file_list)




if __name__ == "__main__":
    main()