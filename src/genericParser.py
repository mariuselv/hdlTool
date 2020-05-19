"""
========================================================
    Filename: genericParser.py
    Author: Marius Elvegård
    Description:

    (c) 2019 Marius Elvegård
========================================================
"""


class GenericParser:

    def __init__(self, tokens):
        self.generic_list   = []
        self._create_generic_list(tokens)

    
    def getGenericList(self):
        return self.generic_list


    def _create_generic_list(self, tokens):
        generics_start = False
        generics_end   = False
        generics_list  = []

        for idx, token in enumerate(tokens):
            tokenUpper = [t.upper() for t in token]


            # List of generics constants will follow
            if tokenUpper == ["KEYWORD", "GENERIC"]:
                generics_start = True

            # We read parse generics until closing bracket is found
            if generics_start:

                if tokenUpper == ["KEYWORD", "PORT"]:
                    generics_end    = True
                    generics_start  = False
                elif tokenUpper == ["KEYWORD", "END"]:
                    generics_end    = True
                    generics_start  = False

            if generics_start and (idx < len(tokens)-1):

                if tokens[idx+1] == ["SYMBOL", ":"]:
                    generic_name = tokens[idx][1]

                elif tokens[idx-1] == ["SYMBOL", ":"]:
                    generic_type = tokens[idx][1]
                    generics_list.append([generic_name, generic_type])

            # No more generics - exit
            if generics_end:
                break

        return generics_list
