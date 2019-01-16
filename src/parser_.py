# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

from error import SolarError

class Parser():
    def __init__(self):
        self.tokens = []
        self.current = 0
        self.ast = {
            "type": "Program",
            "body": []
        }
        
        
    def parse(self, tokens):
        self.tokens = tokens
        self.current = 0
        while self.current < len(self.tokens):
            self.ast["body"].append(self.parseExpression())
        return self.ast
            
        
    def parseExpression(self):
        token = self.tokens[self.current]
        if token["type"] == "number":
            return self.parseLiteral("NumberLiteral")
        if token["type"] == "string":
            return self.parseLiteral("StringLiteral")
        if token["type"] == "bool":
            return self.parseLiteral("BoolLiteral")
        if token["type"] == "null":
            return self.parseLiteral("NullLiteral")
        if token["type"] == "name":
            return self.parseVariable()
        if token["type"] == "paren" and token["value"] == "(":
            return self.parseCall()
            
        raise SolarError(f"Parse error: Expected expression at '{token['value']}'.")
           
                         
    def parseLiteral(self, literalType):
        token = self.tokens[self.current]
        self.current += 1
        return {
            "type": literalType,
            "value": token["value"]
        }
         
                         
    def parseVariable(self):
        token = self.tokens[self.current]
        self.current += 1
        return {
            "type": "VariableExpression",
            "value": token["value"]
        }
            
                         
    def parseCall(self):
        self.current += 1
        
        try:
            name = self.tokens[self.current]["value"]
        except IndexError:
            name = ""

        # Only a 'name' token may be used as a function name
        if name != "" and self.tokens[self.current]["type"] != "name":
            raise SolarError("Parse error: Expected function name.")

        self.current += 1

        params = []
        
        try:
            token = self.tokens[self.current]
            while token["type"] != "paren" or (token["type"] == "paren" and token["value"] != ")"):
                params.append(self.parseExpression())
                token = self.tokens[self.current]
        except IndexError:
            raise SolarError("Parse error: Expected ')' after function call.")
        
        # Eat the closing paren
        self.current += 1

        return {
            "type": "CallExpression",
            "name": name,
            "params": params
        }
