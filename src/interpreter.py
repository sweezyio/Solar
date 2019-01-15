# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

from error import SolarError

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
        
        try:
            function = self.environment[functionName]
        except KeyError:
            raise SolarError(f"Runtime error: Undefined function '{functionName}'.")

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

                        
# --- Functions in environment --- #

# Name: '+'
def add(args):
    assert(len(args) == 2)
    return args[0] + args[1]

  
# Name: '-'
def subtract(args):
    assert(len(args) == 2)
    return args[0] - args[1]

  
# Name: '*'
def multiply(args):
    assert(len(args) == 2)
    return args[0] * args[1]

  
# Name: '/'
def divide(args):
    assert(len(args) == 2)
    return args[0] / args[1]

  
# Name: '%'
def modulo(args):
    assert(len(args) == 2)
    return args[0] % args[1]

                        
# Name: 'int'
def integer(args):
    assert(len(args) == 1)
    return int(args[0])

                        
# Name: 'float'
def decimal(args):
    assert(len(args) == 1)
    return float(args[0])

                        
# Name: 'str'
def string(args):
    assert(len(args) == 1)
    return str(args[0])

  
# Name: 'put'
def put(args):
    assert(len(args) == 1)
    print(args[0])
    return args[0]
  
# --- End functions in environment --- #
