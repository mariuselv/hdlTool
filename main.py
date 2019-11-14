import sys



sys.path.insert(0, 'dep')
from parser import Parser
from lexer import Lexer
from finder import Finder
from vhd import VHD


def present(file_item, id, dependency):
    print("\n")
    print("File: %s" %(file_item))

    if len(id) > 0:
        print("%s: %s" %(id[0][0], id[0][1]))
    for item in dependency:
        print("  %s: %s" %(item[0], item[1]))
    print("\n")


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
        id         = parser.get_id()

        # Save file item
        vhd_file.set_dependency(dependency)
        vhd_file.set_entity(id)

        vhd_files.append(vhd_file)

        present(file_item, id, dependency)



def main():
    finder = Finder()
    finder.add_files("test/*.vhd")
    file_list = finder.get_files()

    colonize(file_list)




if __name__ == "__main__":
    main()