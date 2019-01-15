# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

from error import SolarError

class Interpreter:
    def __init__(self):
        self.functions = {
            "+": lambda args: self.add(args),
            "-": lambda args: self.subtract(args),
            "*": lambda args: self.multiply(args),
            "/": lambda args: self.divide(args),
            "%": lambda args: self.modulo(args),
            "int": lambda args: self.integer(args),
            "float": lambda args: self.decimal(args),
            "str": lambda args: self.string(args),
            "put": lambda args: self.put(args),
            "=": lambda args: self.equals(args),
            ">": lambda args: self.greater(args),
            "<": lambda args: self.less(args),
            "lower": lambda args: self.lower(args),
            "upper": lambda args: self.upper(args),
            "encode": lambda args: self.enc(args),
            "decode": lambda args: self.dec(args),
            "set": lambda args: self.setVariable(args),
        }
        self.variables = {}


    def getVariable(self, expression):
        name = expression["value"]

        try:
            return self.variables[name]
        except KeyError:
            raise SolarError(f"Runtime error: Undefined variable {name}.")

                        
    def call(self, expression):
        functionName = expression["name"]
        
        try:
            function = self.functions[functionName]
        except KeyError:
            raise SolarError(f"Runtime error: Undefined function '{functionName}'.")

        return function(expression["params"])

                        
    def evaluate(self, expression):
        typ = expression["type"]

        if typ == "NumberLiteral":
            return expression["value"]
        elif typ == "StringLiteral":
            return expression["value"]
        elif typ == "VariableExpression":
            return self.getVariable(expression)
        elif typ == "CallExpression":
            return self.call(expression)

    def interpret(self, program):
        for expression in program["body"]:
            self.evaluate(expression)

                        
    # --- Functions in environment --- #

    # Name: 'set'
    def setVariable(self, args):
        assert(len(args) == 2)

        name = args[0]

        if name["type"] != "VariableExpression":
            raise SolarError("Can only assign to variable names.")

        self.variables[name["value"]] = self.evaluate(args[1])   


    # Name: '+'
    def add(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) + self.evaluate(args[1])

  
    # Name: '-'
    def subtract(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) - self.evaluate(args[1])

  
    # Name: '*'
    def multiply(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) * self.evaluate(args[1])

  
    # Name: '/'
    def divide(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) / self.evaluate(args[1])

  
    # Name: '%'
    def modulo(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) % self.evaluate(args[1])

                        
    # Name: 'int'
    def integer(self, args):
        assert(len(args) == 1)
        return int(self.evaluate(args[0]))

                        
    # Name: 'float'
    def decimal(self, args):
        assert(len(args) == 1)
        return float(self.evaluate(args[0]))

                        
    # Name: 'str'
    def string(self, args):
        assert(len(args) == 1)
        return str(self.evaluate(args[0]))

  
    # Name: 'put'
    def put(self, args):
        assert(len(args) == 1)
        val = self.evaluate(args[0])
        print(val)
        return val

    # Name '='

    def equals(self, args):
        assert(len(args) == 2)
        return args[0] == args[1]

    # Name '>'


    def greater(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) > self.evaluate(args[1])

    # Name '<'

    def less(self, args):
        assert(len(args) == 2)
        return self.evaluate(args[0]) < self.evaluate(args[1])

    # Name 'lower'

    def lower(self, args):
        assert(len(args) == 1)
        return self.evaluate(args[0]).lower()

    # Name 'upper'

    def upper(self, args):
        assert(len(args) == 1)
        return self.evaluate(args[0]).upper()

    # Name 'encode'

    def enc(self, args):
        assert(len(args) == 1)
        li = []
        for i in self.evaluate(args[0]):
            li.append(ord(i))
        return li

    # Name 'decode'

    def dec(self, args):
        assert(len(args) == 1)
        if isdigit(args[0]):
            return chr(self.evaluate(args[0]))
        else:
            raise RuntimeError(f"Invalid Character {args[0]}, must be numeric.")
  
# --- End functions in environment --- #
