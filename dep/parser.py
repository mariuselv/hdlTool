"""
========================================================
    Filename: parser.py
    Author: Marius Elvegård
    Description:


========================================================
"""

_dep_keywords = ["library", "use", "context", "component", "entity"]
_id_keywords  = ["entity", "package"]
_symbols = ["(", ")", "[", "]", ";", ",", "."]



class Parser():

    def __init__(self, tokens):
        self.tokens = tokens

    def get_dependency(self):
        dependency_list = []
        token_counter = 0
        
        while token_counter < len(self.tokens)-1:
            token_keyword   = self.tokens[token_counter][0]
            token_word      = self.tokens[token_counter][1]

            # Find VHDL keywords
            if token_keyword == "KEYWORD":

                # Check if token is a dependency keyword and save it
                if token_word.lower() in _dep_keywords:
                    tokens_item = self.tokens[token_counter+1][1]

                    # Catch any component instantiations in architecture
                    if "." in tokens_item:
                        idx = tokens_item.index(".")+1
                        tokens_item = tokens_item[idx:]

                    dependency_list.append(["DEPENDENCY_" + token_word.upper(), tokens_item])

            token_counter += 1

        return dependency_list




    def get_type(self):
        type_list = []
        token_counter = 0
        while token_counter < len(self.tokens)-1:
            token_keyword   = self.tokens[token_counter][0]
            token_word      = self.tokens[token_counter][1]

            # Find VHDL keywords
            if token_keyword == "KEYWORD":

                # Check if token is a entity keyword and save the first found
                if token_word.lower() in _id_keywords:
                    type_list.append([token_word.upper(),  self.tokens[token_counter+1][1]])
                    # Done
                    break

            token_counter += 1

        if not( type_list ):
            type_list.append(["OTHER", "OTHER"])

        return type_list
