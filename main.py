# inp means input, as in and input are keywords
def lexer(inp):
    current = 0
    tokens = []
    while current < len(inp):
        char = inp[current]

        if char == "(":
            tokens.append({
                "type": "paren",
                "value": "(",
            })
            current += 1
            continue

        if char == ")":
            tokens.append({
                "type": "paren",
                "value": ")",
            })
            current += 1
            continue

        """if char == "[":
            tokens.append({
                "type": "bracket",
                "value": "[",
            })
            current += 1
            continue
        if char == "]":
            tokens.append({
                "type": "bracket",
                "value": "]",
            })
            current += 1
            continue
        if char == "{":
            tokens.append({
                "type": "curly",
                "value": "{",
            })
            current += 1
            continue
        if char == "}":
            tokens.append({
                "type": "curly",
                "value": "}",
            })
            current += 1
            continue
        
        if char == "+":
            tokens.append({
                "type": "oper",
                "value": "+",
            })
            current += 1
            continue
        if char == "-":
            tokens.append({
                "type": "oper",
                "value": "-",
            })
            current += 1
            continue
        if char == "/":
            tokens.append({
                "type": "oper",
                "value": "/",
            })
            current += 1
            continue
        if char == "*":
            tokens.append({
                "type": "oper",
                "value": "*",
            })
            current += 1
            continue
        
        if char == "=":
            
            tokens.append({
                "type": "oper",
                "value": "=",
            })
            current += 1
            continue
        
        if char == "~":
            tokens.append({
                "type": "oper",
                "value": "~",
            })
            current += 1
            continue"""

        if char == "`":
            current += 1
            char = inp[current]
            while char != '`':
                current += 1
                char = inp[current]
            current += 1
            char = inp[current]
            continue

        whitespace = ["\n", "\t", " "]
        if char in whitespace:
            current += 1
            continue

        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if char in numbers:
            value = ""
            while char in numbers:
                value += char
                current += 1
                char = inp[current]
            tokens.append({
                "type": "number",
                "value": int(value),
            })
            continue

        if char == '"':
            value = ""
            current += 1
            char = inp[current]
            while char != '"':
                value += char
                current += 1
                char = inp[current]
            current += 1
            char = inp[current]
            tokens.append({
                "type": "string",
                "value": value,
            })
            continue

        if char == "'":
            value = ""
            current += 1
            char = inp[current]
            while char != "'":
                value += char
                current += 1
                char = inp[current]
            current += 1
            char = inp[current]
            tokens.append({
                "type": "string",
                "value": value,
            })
            continue

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '$']
        if char.lower() in letters:
            value = ""
            while char.lower() in letters:
                value += char.lower()
                current += 1
                char = inp[current]
            tokens.append({
                "type": "name",
                "value": value,
            })
            continue

        raise TypeError("I don't know what this character is: " + char)

    return tokens


def parser(tokens):

    global parserCurrent

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
            "add": lambda args: add(args),
            "subtract": lambda args: subtract(args),
            "multiply": lambda args: multiply(args),
            "divide": lambda args: divide(args),
            "modulo": lambda args: modulo(args),
            "int": lambda args: integer(args),
            "float": lambda args: decimal(args),
            "str": lambda args: string(args),
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
            print(self.evaluate(expression))

# Runs the interpreter


def run(inp):
    ast = parser(lexer(inp))
    print("--START AST--")
    print(ast)
    print("--END AST--\n")
    interpreter = Interpreter()
    interpreter.interpret(ast)

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
    return args[0]
# End functions in environment


parserCurrent = 0
run("(add 1 (modulo 6 4))")
input()
