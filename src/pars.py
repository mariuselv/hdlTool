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

    def get_dependency(self) -> list :
        """  Create a dependency list from the tokens """
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


    def get_type(self) -> list :
        """ Get type of VHD object, e.g. context file, entity or package """
        for token_counter, token in enumerate(self.tokens):
            token_keyword   = token[0]
            token_word      = token[1].upper()
            next_token      = None
            if token_counter < len(self.tokens): 
                next_token = self.tokens[token_counter+1]

            # Find VHDL keywords
            if (token_keyword == "KEYWORD") and (token_word in hdlTool_pkg.id_keywords):
                if token_word == "ENTITY":
                    return [token_word,  next_token[1]]
                elif token_word == "PACKAGE":
                    return [token_word,  next_token[1]]
                elif token_word == "CONTEXT":
                    # Check is next token is "IS"
                    if self.tokens[token_counter+2][0] == "KEYWORD":
                        if self.tokens[token_counter+2][1].upper() == "IS":
                            return[token_word, next_token[1]]
        return ["OTHER", "OTHER"]
