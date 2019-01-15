![Solar Logo](https://github.com/Solar-language/Solar/blob/master/media/Solar-Logo.png?raw=true)

# Solar Docs - Reserved Names

The official solar documentation designed so the team knows what is going on and so that you can learn the language.

## Table of Contents

- [About Solar](#about-solar)
- [Reserved Names](#reserved-names)
	- [Reserved Variable Names](#reserved-variable-names)
	- [Reserved Function Names](#reserved-function-names)
## About Solar

Solar is a Lisp-Style language that uses built-in functions to run everything, making the syntax easy to pick up and not take up too much space.

## Reserved Names

In the topic of reserved names, we will split it up into two parts: Reserved Variable Names and Reserved Function Names, we will start with the smaller Reserved variable names.

### Keywords
These reserved names below are neither functions nor variables; rather they are keywords built in to the language:
```

| Name   | Usage                   | Implemented? |
|:------:|:-----------------------:|:------------:|
|true|True boolean value|Yes|
|false|False boolean value|Yes|
|null|Null value|Yes|
```

### Reserved Variable Names 

| Name   | Usage                   | Implemented? |
|:------:|:-----------------------:|:------------:|
|datetime|Display the time and date| No|

Unfinished...

### Reserved Function Names

| Name   | Usage                   | Implemented? |
|:------:|:-----------------------:|:------------:|
|        |**Operators**            |    |
|+       |Add                      | Yes|
|-       |Subtract                 | Yes|
|*       |Multiply                 | Yes|
|/       |Divide                   | Yes|
|%       |Modulo                   | Yes|
|=       |Equal                    | Yes|
|>       |Greater Than             | Yes|
|<       |Less Than                | Yes|
|>=      |Greater Than or Equal To | No |
|<=      |Less Than or Equal To    | No |
|        |**Variables**         |    |    
|def     |Declare a variable       | Yes |
|set     |Reassign a variable      | Yes |
|        |**Control flow**         |    |
|if      |If expression.           | No |
|elif    |May follow an if expression| No |
|else    |May follow an if or elif expression|No|
|while   |While expression         |No  |
|        |**Converters**           |    |
|lambda  |Creates a lambda object  |No  |
|list    |Return all parameters as a list| No |
|int     |Convert to Integer       | Yes|
|str     |Convert to String        | Yes|
|float   |Convert to Float         | Yes|
|bool    |Convert to Bool         | No|
|lower   |Convert to Lowercase     | Yes|
|upper   |Convert to Uppercase     | Yes|
|encode  |Convert Text to Unicode  | Yes|
|decode  |Convert Unicode to Text  | Yes|
|        |**I/O**                  |    |
|put     |Print output             | Yes|
|get     |Read a line of input from stdin| Yes |
|        |**Errors**               |    |
|raise   |Raise a SolarError   | Yes |

More coming soon...

- The Solar Team

