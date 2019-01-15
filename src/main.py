# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

import sys

from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

from error import SolarError
        
    
def run(inp):
    tokens = Lexer().lex(inp)
    ast = Parser().parse(tokens)

    print("--START AST--")
    print(ast)
    print("--END AST--\n")

    Interpreter().interpret(ast)

                        
def runRepl():
    while True:
        try:
            run(str(input("solar > ")))
        except SolarError as error:
            print(error)
            print()
        except KeyboardInterrupt:
            print("\nQuitting...")
            sys.exit(1)
        except:
            print("Internal error, raising exception:")
            raise

                        
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
