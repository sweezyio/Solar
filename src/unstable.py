import sys
# inp means input, as in and input are keywords

class Lexer():
    def __init__(self):
        self.current = 0
        self.tokens = []
        self.inp = ""
        
    def lex(self, inp):
        self.inp = inp
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
                         '$', '+', '-', '/', '*', '%']
            
            if char.lower() in validName:
                self.name()
                continue
                
            raise RuntimeError(f"Unrecognized character {char}.")
        return self.tokens
                
    def skipWhitespace(self):
        while self.current < len(self.inp):
            if self.inp[self.current] in [' ', '\t', '\n', '\r']:
                self.current += 1
                continue
            
            if self.inp[self.current] == '`':
                current += 1
                while self.inp[self.current] != '`':
                    current += 1
                # Consume the closing backtick
                current += 1
                continue
                
            # We didn't find whitespace
            break
                
    def string(self, quote):
        # Consume the opening quote
        self.current += 1
        value = ""
        
        char = self.inp[self.current]
        while char != quote:
            value += char
            self.current += 1
            char = self.inp[self.current]
            
        # Consume the closing quote
        self.current += 1
        
        self.tokens.append({
            "type": "string",
            "value": value,
        })
    
    def number(self):
        value = ""
        while self.inp[self.current] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            value += self.inp[self.current]
            self.current += 1
        self.tokens.append({
            "type": "number",
            "value": int(value),
        })
        
    def name(self):
        validName = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                     'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                     '$', '+', '-', '/', '*', '%']
        value = ""
        while self.inp[self.current].lower() in validName:
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


def parser(tokens):

    global parserCurrent
    parserCurrent = 0

    def walk():
        global parserCurrent
        token = tokens[parserCurrent]
        if token["type"] == 'number':
            parserCurrent += 1
            return {
                "type": "NumberLiteral",
                "value": token["value"],
            }

        if token["type"] == 'string':
            parserCurrent += 1
            return {
                "type": "StringLiteral",
                "value": token["value"],
            }

        if token["type"] == 'paren' and token["value"] == "(":
            parserCurrent += 1
            token = tokens[parserCurrent]
            node = {
                "type": "CallExpression",
                "name": token["value"],
                "params": [],
            }
            parserCurrent += 1
            token = tokens[parserCurrent]
            while token["type"] != "paren" or token["type"] == "paren" and token["value"] != ")":
                node["params"].append(walk())
                token = tokens[parserCurrent]
            parserCurrent += 1
            return node

        raise TypeError(token["type"])
    ast = {
        "type": "Program",
        "body": [],
    }

    while parserCurrent < len(tokens):
        ast["body"].append(walk())

    return ast


class Interpreter:
    def __init__(self):
        self.environment = {
            "+": lambda args: add(args),
            "-": lambda args: subtract(args),
            "*": lambda args: multiply(args),
            "/": lambda args: divide(args),
            "%": lambda args: modulo(args),
            "int": lambda args: integer(args),
            "float": lambda args: decimal(args),
            "str": lambda args: string(args),
            "put": lambda args: put(args),
        }

    def call(self, expression):
        functionName = expression["name"]
        function = self.environment[functionName]

        params = []
        for param in expression["params"]:
            params.append(self.evaluate(param))

        return function(params)

    def evaluate(self, expression):
        typ = expression["type"]

        if typ == "NumberLiteral":
            return expression["value"]
        elif typ == "StringLiteral":
            return expression["value"]
        elif typ == "CallExpression":
            return self.call(expression)

    def interpret(self, program):
        for expression in program["body"]:
            self.evaluate(expression)

# Runs the interpreter


def run(inp):
    ast = parser(Lexer().lex)
    print("--START AST--")
    print(ast)
    print("--END AST--\n")
    Interpreter().interpret(ast)

# Functions in environment


def add(args):
    assert(len(args) == 2)
    return args[0] + args[1]


def subtract(args):
    assert(len(args) == 2)
    return args[0] - args[1]


def multiply(args):
    assert(len(args) == 2)
    return args[0] * args[1]


def divide(args):
    assert(len(args) == 2)
    return args[0] / args[1]


def modulo(args):
    assert(len(args) == 2)
    return args[0] % args[1]

# Integer is used for int in Solar


def integer(args):
    assert(len(args) == 1)
    return int(args[0])

# Decimal is used for float in Solar


def decimal(args):
    assert(len(args) == 1)
    return float(args[0])

# String used for str in Solar


def string(args):
    assert(len(args) == 1)
    return str(args[0])


def put(args):  # Equivalent to print in python
    assert(len(args) == 1)
    print(args[0])
    return args[0]
# End functions in environment


parserCurrent = 0

def runRepl():
    while True:
        try:
            run(str(input("solar > ")))
        except KeyboardInterrupt:
            print("\nQuitting...")
            sys.exit(1)
        except:
            print("Error:", sys.exc_info()[1])

def runFile(filename):
    with open(filename) as sourceFile:
        run(sourceFile.read())

def main():
    if len(sys.argv) == 1:
        runRepl()
    elif len(sys.argv) == 2:
        runFile(sys.argv[1])
    else:
        raise RuntimeError("Usage: solar [filename]")

main()
