![Solar Logo](https://github.com/Solar-language/Solar/blob/master/media/Solar-Logo.png?raw=true)

# Solar Docs - Using Functions

The official solar documentation designed so the team knows what is going on and so that you can learn the language.

## Table of Contents

- [Using Functions](#using-functions)
	- [Functions Table](#functions-table)
	- [Functions In-depth](#functions-in-depth)
		- [Operator Functions](#operator-functions)
			- [Arithmetic Operators](#arithmetic-operators)
			- [Comparison Operators](#comparison-operators)
	    - [Converter Functions](#converter-functions)
	    - [I/O Functions](#io-functions)

## Using Functions

Functions power the whole language in Solar, so knowing how to use functions is very useful, for people who just want to skim, I have left the table from Reserved names in here so that you can easily find functions, as well as an In-depth explanation of what the functions do.
 
### Functions Table

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
|        |**Converters**           |    |
|int     |Convert to Integer       | Yes|
|str     |Convert to String        | Yes|
|float   |Convert to Float         | Yes|
|lower   |Convert to Lowercase     | Yes|
|upper   |Convert to Uppercase     | Yes|
|encode  |Convert Text to Unicode  | Yes|
|decode  |Convert Unicode to Text  | Yes|
|        |**I/O**           |    |
|put     |Print output             | Yes|
|get     |Print input              | No |
|set     |Set a variable           | Yes|

### Functions In-Depth

We are going to split the In-depth functions into three main parts, **Operators**, **Converters** and **I/O**.

#### Operator Functions

We will split Operator functions into Arithmetic and Comparison Operators. When in the syntax you do **not** need the angled brackets `<>`.

##### Arithmetic Operators

1. **+**

The + operator is used for adding two numbers or joining two strings together. 

Syntax: `(+ <value 1> <value 2>)`

Example: 
```
(put (+ 1 3))
```
Output:
```
4
```

2. **-**

The - operator is used for subtracting one number from another.

Syntax: `(- <value 1> <value 2>)`

Example:

```
(put (- 4 3))
```

Output:

```
1
```

3. __*__

This operator is used for multiplying two numbers.

Syntax: `(* <value 1> <value 2>)`

Example:

```
(put (* 3 5))
```

Output:

```
15
```

4. **/**

This operator is used for dividing one number by another.

Syntax: `(/ <value 1> <value 2>)`

Example:

```
(put (/ 15 3))
```

Output:

```
5
```

5. **%**

This operator is used for finding the remainder after two numbers are divided to an integer.

Syntax: `(% <value 1> <value 2>)`

Example:

```
(put (% 6 4))
```

Output:

```
2
```
##### Comparison Operators
1. **=**

This operator is used for finding if two values are equal.

Syntax: `(= <value 1> <value 2>)`

Example:

```
(put (= 4 4))
```

Output:

```
True
```

2. **>**

This operator is used for finding if the first value is bigger.

Syntax: `(> <value 1> <value 2>)`

Example:

```
(put (> 4 6))
```

Output:

```
False
```

3. **<**

This operator is used for finding if the first value is smaller.

Syntax: `(< <value 1> <value 2>)`

Example:

```
(put (< 8 4))
```

Output:

```
False
```

4. **>=**

This operator is used for finding if the first value is larger than or equal to the second.

Syntax: `(>= <value 1> <value 2>)`

Example:

```
(put (>= 8 8))
```

Output:

```
True
```

5. **<=**

This operator is used for finding if the first value is smaller than or equal to the second.

Syntax: `(<= <value 1> <value 2>)`

Example:

```
(put (<= 8 6))
```

Output:

```
False
```
#### Converter Functions
1. **int**

Converts a value to an int.

Syntax: `(int <value 1>)`

Example:

```
(put (+ "8" "8"))
(put (+ (int "8") (int "8")))
```

Output:

```
88
16
```

2. **str**

Converts a value to an String.

Syntax: `(str <value 1>)`

Example:

```
(put (+ 24 6))
(put (+ (str 24) (str 6)))
```

Output:

```
30
246
```

3. **float**

Converts a value to a float.

Syntax: `(float <value 1>)`

Example:

```
(put (+ "8.1" "8.1"))
(put (+ (float "8.1") (float "8.1")))
```

Output:

```
8.18.1
16.2
```

4. **lower**

Converts a string to lowercase.

Syntax: `(lower <value 1>)`

Example:

```
(put (lower "Hello, World!"))
```

Output:

```
hello, world!
```

5. **upper**

Converts a string to lowercase.

Syntax: `(upper <value 1>)`

Example:

```
(put (upper "Hello, World!"))
```

Output:

```
HELLO, WORLD!
```

6. **encode**

Converts a string to Unicode base 10.

Syntax: `(encode <value 1>)`

Example:

```
(put (encode "Hello, World!"))
```

Output:

```
[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
```

6. **decode**

Converts a unicode base 10 number to a char.

Syntax: `(decode <value 1>)`

Example:

```
(put (decode 72))
```

Output:

```
H
```

#### I/O Functions

1. **put**

Prints a value

Syntax: `(put <value 1>)`

Example:

```
(put "Hello, World!")
```

Output:

```
Hello, World!
```

2. **get**

Gets the next line of input.

Syntax: `(get <value 1 (optional)>)`

Example:

```
(get "Hello, World! > ")
```

Output:

```
Hello, World! > 
```

2. **set**

Sets a variable.

Syntax: `(get <value 1> <value 2>)`

Example:

```
(set x "Hello, World!")
(put x)
```

Output:

```
Hello, World! 
```

- The Solar Team
