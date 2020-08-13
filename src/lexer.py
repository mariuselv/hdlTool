"""
========================================================
    Filename: lexer.py
    Author: Marius Elvegaard
    Description:

    (c) 2019 Marius Elvegaard
========================================================
"""


import re
import hdlTool_pkg



class Lexer(object):
    tokens = []

    def __init__(self, source_code):
        # String
        source_code = self._string_to_list(source_code)
        self.tokens = self.tokenize(source_code)

    def _complete_string(self, str, str_char='\"'):
        is_complete = True
        for c in str:
            if c == str_char:
                is_complete = not(is_complete)
        return is_complete

    def _string_to_list(self, source_code):
        """ Creating word list of source code """
        return re.findall(r'\S+|\n', source_code)

    def tokenize(cls, source_code) -> list :
        """ Create tokens list from source code string """
        tokens = []
        
        # Word index counter
        source_index = 0

        # Counters
        line_number = 1
        word_number = 1

        # Set to True when parsing inside a string
        in_string = False
        # Set to True when parsing inside a comment
        in_comment = False

        # Loop words in source code and generate tokens
        while source_index < len(source_code):
            word = source_code[source_index]

            statement_end = False

            # New line detected: reset
            if '\n' == word:
                tokens.append(["NEW_LINE", '\n', line_number, word_number])
                in_comment = False
                in_string = False


            # Check if this is the start of a comment line
            if (word[0:2] == "--") and not(in_string) and not(in_comment):
                tokens.append(["SYMBOL", word[0:2], line_number, word_number])
                in_comment = True

                # Check if this is the end of the comment line
                if word[len(word)-2] == '\n':
                    in_comment = False
                    tokens.append(["COMMENT", word[:len(word)-2], line_number, word_number])
                    tokens.append(["NEW_LINE", '\n', line_number, word_number])
                # Check if comment is right after comment identifier
                elif len(word) > 2:
                    tokens.append(["COMMENT", word[2:], line_number, word_number])

            # This is an active comment line
            elif in_comment:
                tokens.append(["COMMENT", word, line_number, word_number])
                if word[len(word)-1] == '\n':
                    in_comment = False
                    tokens.append(["NEW_LINE", '\n', line_number, word_number])


            # Detect code strings
            elif (word in hdlTool_pkg.string) and not(in_string):
                in_string = True
                tokens.append(["SYMBOL", word, line_number, word_number])
            elif (word in hdlTool_pkg.string) and in_string:
                in_string = False
                tokens.append(["SYMBOL", word, line_number, word_number])
            elif in_string:
                tokens.append(["STRING", word, line_number, word_number])
            # Need checks for strings of type: "foo", not only: "foo  and foo"


            elif not(in_string) and not(in_comment):

                # Remove statement ending ';' from word, will be added later
                if word[len(word)-1] == ";":
                    statement_end = True
                    word = word[:len(word)-1]

                if word.lower() in hdlTool_pkg.keywords:
                    tokens.append(["KEYWORD", word, line_number, word_number])

                elif word.lower() in hdlTool_pkg.commons:
                    tokens.append(["COMMON_KEYWORD", word, line_number, word_number])

                elif word in hdlTool_pkg.assignment:
                    tokens.append(["ASSIGNMENT", word, line_number, word_number])

                elif word in hdlTool_pkg.operator:
                    tokens.append(["OPERATOR", word, line_number, word_number])

                elif word in hdlTool_pkg.symbols:
                    tokens.append(["SYMBOL", word, line_number, word_number])

                elif re.match('[0-9]', word):
                    tokens.append(["INTEGER", word, line_number, word_number])

                elif re.match('[a-z]', word.lower()):
                    tokens.append(["IDENTIFIER", word, line_number, word_number])

                elif word in hdlTool_pkg.comments:
                    tokens.append(["COMMENT", word, line_number, word_number])

                elif word in hdlTool_pkg.new_line:
                    tokens.append(["NEW_LINE", "\n", line_number, word_number])

                else:
                    if not('\n') in word:
                        tokens.append(["UNKNOWN", word, line_number, word_number])

                if statement_end:
                   tokens.append(["STATEMENT_END", ";", line_number, word_number])

            if tokens[len(tokens)-1][0] == "NEW_LINE":
                line_number += 1
                word_number = 1
            else:
                word_number += 1

            # Increment word index counter
            source_index += 1

        return tokens


    def get_tokens(self) -> list :
        return self.tokens
