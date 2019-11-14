
_dep_keywords = ["library", "use", "context", "component"]
_id_keywords  = ["entity", "package"]

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
                    dependency_list.append(["DEPENDENCY_" + token_word.upper(), self.tokens[token_counter+1][1]])

            token_counter += 1

        return dependency_list

    def get_id(self):
        id_list = []
        token_counter = 0
        while token_counter < len(self.tokens)-1:
            token_keyword   = self.tokens[token_counter][0]
            token_word      = self.tokens[token_counter][1]

            # Find VHDL keywords
            if token_keyword == "KEYWORD":
                # Check if token is a entity keyword and save the first found
                if token_word.lower() in _id_keywords:
                    id_list.append([token_word.upper(),  self.tokens[token_counter+1][1]])

                    # Done
                    break

            token_counter += 1

        return id_list
