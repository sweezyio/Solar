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
        while self.current < len(self.tokens):
            self.ast["body"].append(self.parseExpression())
        return self.ast
            
        
    def parseExpression(self):
        token = self.tokens[self.current]
        if token["type"] == "number":
            return self.parseNumber()
        if token["type"] == "string":
            return self.parseString()
        if token["type"] == "paren" and token["value"] == "(":
            return self.parseCall()
            
        raise TypeError(f"Expected expression at '{token['value']}'.")
           
                        
    def parseNumber(self):
        token = self.tokens[self.current]
        self.current += 1
        return {
            "type": "NumberLiteral",
            "value": token["value"]
        }
              
                        
    def parseString(self):
        token = self.tokens[self.current]
        self.current += 1
        return {
            "type": "StringLiteral",
            "value": token["value"]
        }
         
                        
    def parseCall(self):
        self.current += 1
        name = self.tokens[self.current]["value"]
        self.current += 1

        params = []
        
        token = self.tokens[self.current]
        while token["type"] != "paren" or (token["type"] == "paren" and token["value"] != ")"):
            params.append(self.parseExpression())
            token = self.tokens[self.current]
        
        # Eat the closing paren
        self.current += 1

        return {
            "type": "CallExpression",
            "name": name,
            "params": params
        }
