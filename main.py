import sys



sys.path.insert(0, 'dep')
from parser import Parser
from lexer import Lexer
from finder import Finder



def main():
    #finder = Finder()
    #finder.add_files("test/*.vhd")
    #file_list = finder.get_files()
    tokens = []


    with open("test/uart_vvc.vhd", 'r') as file:
        content = file.read() 
    
    # Lexer
    print("Running Lexer")
    lex = Lexer(content)
    tokens = lex.tokenize()
    
    # Parser
    print("Running parser")
    parser = Parser(tokens)
    dependency = parser.get_dependency()
    entity = parser.get_entity()

    print(dependency)
    print(entity)


if __name__ == "__main__":
    main()