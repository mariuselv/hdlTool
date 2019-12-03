"""
========================================================
    Filename: parser.py
    Author: Marius Elvegård
    Description:


========================================================
"""

_dep_keywords = ["LIBRARY", "USE", "CONTEXT", "COMPONENT", "ENTITY"]
_id_keywords  = ["ENTITY", "PACKAGE", "CONTEXT"]
_symbols = ["(", ")", "[", "]", ";", ",", "."]



class Parser():

    def __init__(self, tokens):
        self.tokens = tokens

    def get_dependency(self):
        """
        Create a dependency list from the tokens
        """
        dependency_list = []
        token_counter = 0
        
        while token_counter < len(self.tokens)-1:
            token_keyword   = self.tokens[token_counter][0].upper()
            token_word      = self.tokens[token_counter][1].upper()

            # Find VHDL keywords
            if token_keyword == "KEYWORD":

                # Check if token is a dependency keyword and save it
                if token_word in _dep_keywords:
                    tokens_item = self.tokens[token_counter+1][1]

                    # Catch any component instantiations in architecture
                    if "." in tokens_item:
                        idx = tokens_item.index(".")+1
                        tokens_item = tokens_item[idx:]

                    dependency_list.append(["DEPENDENCY_" + token_word, tokens_item])

            token_counter += 1

        return dependency_list



    def get_type(self):
        """ 
        Get type of VHD object, e.g. context file, entity or package
        """
        type_list = []
        token_counter = 0

        while (token_counter < len(self.tokens)-1):
            token_keyword   = self.tokens[token_counter][0]
            token_word      = self.tokens[token_counter][1].upper()

            # Find VHDL keywords
            if (token_keyword == "KEYWORD") and (token_word in _id_keywords):
                
                if token_word in _id_keywords:

                    # ENTITY ?
                    if token_word == "ENTITY":
                        type_list = [[token_word,  self.tokens[token_counter+1][1]]]
                        # Done
                        break
                    
                    # PACKAGE ?
                    elif token_word == "PACKAGE":
                        type_list = [[token_word,  self.tokens[token_counter+1][1]]]
                        # Done
                        break
                        
                    # CONTEXT ?
                    elif token_word == "CONTEXT":
                        # Check is next token is "IS"
                        if self.tokens[token_counter+2][0] == "KEYWORD":
                            if self.tokens[token_counter+2][1].upper() == "IS":
                                type_list = [[token_word, self.tokens[token_counter+1][1]]]
                                break

            token_counter += 1

        if not( type_list ):
            type_list.append(["OTHER", "OTHER"])

        return type_list
