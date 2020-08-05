"""
========================================================
    Filename: parser.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""

import hdlTool_pkg


class Parser():

    def __init__(self, tokens):
        self.tokens = tokens

    def get_dependency(self):
        """
        Create a dependency list from the tokens
        """
        dependency_list = []
        token_counter = 0
        is_comment = False
        is_string  = False
        
        while token_counter < len(self.tokens)-1:
            token_keyword   = self.tokens[token_counter][0].upper()
            token_word      = self.tokens[token_counter][1].upper()

            # Skip any string as these can contain VHDL reserved keywords
            if token_keyword == "SYMBOL" and token_word == "\"":
                is_string = not(is_string)

            # Skip any comments as these can contain VHDL reserved keywords
            if token_keyword == "COMMENT" and token_word[0:2] == "--":
                is_comment = True
            if token_keyword == "NEW_LINE" and is_comment:
                is_comment = False              


            # Find VHDL keywords
            if token_keyword == "KEYWORD" and not(is_string) and not(is_comment):

                # Check if token is a dependency keyword and save it
                if token_word in hdlTool_pkg.dep_keywords:
                    tokens_item = self.tokens[token_counter+1][1]

                    # Catch any component instantiations in architecture
                    if "." in tokens_item:
                        idx = tokens_item.index(".")+1
                        tokens_item = tokens_item[idx:]

                    dependency_list.append(["DEPENDENCY_" + token_word, tokens_item])
                    token_counter += 1

                # Catch any in-code clauses, e.g. "alias X is my_library.my_pkg.Y"
                elif token_word in hdlTool_pkg.inlines:
                    next_token_keyword = self.tokens[token_counter + 1][0]
                    next_token_word    = self.tokens[token_counter + 1][1]
                    if next_token_keyword.upper() == "IDENTIFIER":

                        # Need to find a referenced signal/constant/type etc
                        #   <library>.<package>.<signal/constant/type>
                        if next_token_word.count(".") > 1:
                            # Remove libray part (<package>.<signal/constant/type>)
                            dep = next_token_word[next_token_word.index(".")+1:]                            
                            # Remove everything from next "." (<package>)
                            dep = dep[:dep.index(".")]
                            dependency_list.append(["DEPENDENCY_USE", dep])
                            token_counter += 1

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
            if (token_keyword == "KEYWORD") and (token_word in hdlTool_pkg.id_keywords):
                
                if token_word in hdlTool_pkg.id_keywords:

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
