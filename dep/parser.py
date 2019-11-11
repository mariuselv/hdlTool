
_dep_keywords = ["library", "use", "context", "component", "package"]


class Parser():


    def __init__(self, tokens):
        self.tokens = tokens


    def dependencies(self):
        dep = []
        token_counter = 0
        
        while token_counter < len(self.tokens)-1:
            token_keyword   = self.tokens[token_counter][0]
            token_word      = self.tokens[token_counter][1]

            # Find VHDL keywords
            if token_keyword == "KEYWORD":

                # Check if token it a dependency keyword and save it
                if token_word.lower() in _dep_keywords:
                    dep.append(["DEPENDENCY_" + token_word.upper(), self.tokens[token_counter+1][1]])
                    print(token_keyword + " : " + token_word + " = " + self.tokens[token_counter+1][1])

            token_counter += 1


        return dep