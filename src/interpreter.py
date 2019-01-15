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
  
# --- End functions in environment --- #
