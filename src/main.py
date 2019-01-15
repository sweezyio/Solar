# The Solar Programming Language
# https://github.com/Solar-language/Solar

# Licensed under the MIT Licence.
# See https://github.com/Solar-language/Solar/blob/master/LICENSE.md

import sys

import solarLexer
import solarParser
import solarInterpreter
        
    
def run(inp):
    tokens = solarLexer.Lexer().lex(inp)
    ast = solarParser.Parser().parse(tokens)

    print("--START AST--")
    print(ast)
    print("--END AST--\n")

    solarInterpreter.Interpreter().interpret(ast)

                        
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
