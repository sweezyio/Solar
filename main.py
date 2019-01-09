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

        raise TypeError(token.type)
    ast = {
        "type": "Program",
        "body": [],
    }

    while parserCurrent < len(tokens):
        ast["body"].append(walk())

    return ast


parserCurrent = 0
print(parser(lexer("(add 1 (subtract 2 1))")))
input()
