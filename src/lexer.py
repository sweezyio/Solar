# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

from error import SolarError

class Lexer():
    def __init__(self):
        self.current = 0
        self.tokens = []
        self.inp = ""
        
        
    def lex(self, inp):
        self.inp = inp
        self.current = 0
        while self.current < len(self.inp):
            self.skipWhitespace()
            char = self.inp[self.current]
            
            # Single character tokens
            if char == "(":
                self.addToken("paren", "(")
                continue
            if char == ")":
                self.addToken("paren", ")")
                continue
                
            # Strings
            if char == '"':
                self.string('"')
                continue
                
            if char == "'":
                self.string("'")
                continue
                
            # Numbers
            if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                self.number()
                continue
                
            # Names
            validName = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                         '$', '+', '-', '/', '*', '%', '=', '>', '<']
            
            if char.lower() in validName:
                self.name()
                continue
                
            raise SolarError(f"Lexical error: Unrecognized character {char}.")
        return self.tokens
         
        
    def skipWhitespace(self):
        while self.current < len(self.inp):
            if self.inp[self.current] in [' ', '\t', '\n', '\r']:
                self.current += 1
                continue
            
            if self.inp[self.current] == '`':
                current += 1
                try:
                    while self.inp[self.current] != '`':
                        current += 1
                except IndexError:
                    raise SolarError("Lexical error: Unterminated comment.")
                # Consume the closing backtick
                current += 1
                continue
                
            # We didn't find whitespace
            break
             
                
    def string(self, quote):
        # Consume the opening quote
        self.current += 1
        value = ""

        try:
            while self.inp[self.current] != quote:
                value += self.inp[self.current]
                self.current += 1
        except IndexError:
            raise SolarError("Lexical error: Unterminated string.")
            
        # Consume the closing quote
        self.current += 1
        
        self.tokens.append({
            "type": "string",
            "value": value,
        })
    
    
    def number(self):
        value = ""
        while not self.atEnd() and self.inp[self.current] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            value += self.inp[self.current]
            self.current += 1
        self.tokens.append({
            "type": "number",
            "value": int(value),
        })
        

    def name(self):
        validName = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                     '$', '+', '-', '/', '*', '%', '=', '>', '<']
        value = ""
        while not self.atEnd() and self.inp[self.current].lower() in validName:
            value += self.inp[self.current].lower()
            self.current += 1
        self.tokens.append({
            "type": "name",
            "value": value,
        })
        
                
    def addToken(self, typ, value):
        self.tokens.append({
            "type": typ,
            "value": value,
        })
        self.current += len(str(value))


    def atEnd(self):
        return self.current >= len(self.inp)
