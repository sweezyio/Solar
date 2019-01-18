
﻿![Solar Logo](https://github.com/Solar-language/Solar/blob/master/media/solar-logo.png?raw=true)

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
	  - [Variable Functions](#variable-functions)
	  - [Control Flow Functions](#control-flow-functions)
	  - [Other Functions](#other-functions)

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
|!=      |Not equal                | Yes|
|>       |Greater Than             | Yes|
|<       |Less Than                | Yes|
|>=      |Greater Than or Equal To | Yes |
|<=      |Less Than or Equal To    | Yes|
|        |**Variables**         |    |    
|def     |Declare a variable       | Yes |
|set     |Reassign a variable      | Yes |
|append  |Append to a list.        | Yes |
|index   |Get the *n*th value in a list| Yes |
|        |**Control flow**         |    |
|if      |If expression.           | Yes |
|elif    |May follow an if expression| Yes |
|else    |May follow an if or elif expression|Yes|
|while   |While expression         |Yes  |
|        |**Converters**           |    |
|lambda  |Creates a lambda object  |Yes  |
|list    |Return all parameters as a list| Yes |
|int     |Convert to Integer       | Yes|
|str     |Convert to String        | Yes|
|float   |Convert to Float         | Yes|
|bool    |Convert to Bool          | Yes|
|lower   |Convert to Lowercase     | Yes|
|upper   |Convert to Uppercase     | Yes|
|encode  |Convert Text to Unicode  | Yes|
|decode  |Convert Unicode to Text  | Yes|
|        |**I/O**                  |    |
|put     |Print output without new line            | Yes|
|print    |Print output             | Yes|
|get     |Read a line of input from stdin| Yes |
|        |**Other**               |    |
|raise   |Raise a SolarError   | Yes |
|datetime   |Returns the date and/or time   | Yes |
|random   |Returns a random number   | Yes |

### Functions In-Depth

We are going to split the In-depth functions into six main parts, **Operators**, **Converters**, **I/O**, **Variables**, **Control Flow** and **Other**.

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
1. **list**

Takes an unlimited number of parameters and creates a list containing those parameters.

Syntax: `(list <unlimited number of params(optional)>)`

If passed no parameters, it will simply return an empty list.

Example:
```
(print (list))
(print (list 1 2 "foo" true))
```
Output:
```
[]
[1, 2, foo, true]
```

2. **int**

Converts a value to an int.

Syntax: `(int <value 1>)`

Example:

```
(print (+ "8" "8"))
(print (+ (int "8") (int "8")))
```

Output:

```
88
16
```

3. **str**

Converts a value to an String.

Syntax: `(str <value 1>)`

Example:

```
(print (+ 24 6))
(print (+ (str 24) (str 6)))
```

Output:

```
30
246
```

5. **lower**

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

6. **upper**

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

7. **decode**

Converts a string to a list of bytes.

Syntax: `(decode <value 1>)`

Example:

```
(put (decode "Hello, World!"))
```

Output:

```
[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
```

8. **encode**

Converts a list of bytes to a Unicode string.

Syntax: `(encode <value 1>)`

Example:

```
(print (encode 72))
(print (encode (list 72 101 108)))
```

Output:

```
H
Hel
```

9. **lambda**

Creates a lambda object. 

Syntax: `(lambda (params) <unlimited amount of values (optional>)`

Example:

```
(def plus (lambda (x y) (put (+ x y)))
(plus 1 3)
```

Output:

```
4
```
10. **bool**

Converts a value to a Boolean.

Syntax: `(bool <value 1>)`

Example:

```
(put (bool 1))
```

Output:

```
True
```

#### I/O Functions

1. **put**

Prints a value without a newline

Syntax: `(put <value 1>)`

Example:

```
(put "Hello, World!")
(put "Hello, World!")
```

Output:

```
Hello, World!Hello, World!
```

2. **print**:

Prints a value, plus a newline

Syntax: `(print <value 1>)`

Example:
```
(print "foo")
(print "bar")
```
Output:
```
foo
bar
```

3. **get**

Gets a line of input.

Syntax: `(get <value 1 (optional)>)`

Example:

```
(get "Hello, World! > ")
```

Output:

```
Hello, World! > 
```
#### Variable Functions
1. **def**

Defines a variable. Note that you cannot redefine a variable already defined with `def` - but you can reassign its value using
`set`.

Syntax: `(def <value 1> <value 2 (optional)>)`

If value 2 is not provided, the variable will have the value of `null` by default.

Example:
```
(def x)
(put x)

(def y 32)
(put y)
```
Output:
```
null
32
```

2. **set**

Assigns to a variable. Note that a variable must be defined with `def` before it is assigned to with `set`.

Syntax: `(set <value 1> <value 2>)`

Example:

```
(def x "Hello, world!")
(put x)
(set x "Goodbye, world!")
(put x)
```

Output:

```
Goodbye, world! 
```

3. **append**

Appends to a list.

Syntax: `(append <value 1> <value 2>)`

Example:

```
(def x (list "Hi" "Bye"))
(print x)
(append x "Good Luck")
(print x)
```

Output:

```
["Hi", "Bye"]
["Hi", "Bye", "Good Luck"]
```


4. **index**

Finds the *n*th value in a list.

Syntax: `(index <value 1> <value 2>)`

Example:

```
(def x (list "Hi" "Bye" "Good Luck"))
(print (index x 2))
```

Output:

```
Good Luck
```

#### Control-Flow Functions

1. **if**

Checks if the statement is true, and if it is, runs something.

Syntax: `(if <value 1> <value 2> <unlimited amount of values (optional>)`

Example:

```
(if (= 1 1) (print "Hi"))
```

Output:

```
Hi
```

2. **elif**

If the if or elif statement before it is not true, and it is true then runs something.

Syntax: `(elif <value 1> <value 2> <unlimited amount of values (optional>)`

Example:

```
(if (= 1 2) (print "Hi"))(elif (< 1 2) (print "Bye"))
```

Output:

```
Bye
```

3. **else**

If the if or elif statement before it is not true then it runs something.

Syntax: `(else <value 1> <unlimited amount of values (optional>)`

Example:

```
(if (= 1 2) (print "Hi"))(elif (> 1 2) (print "Bye"))(else (print "Good Luck"))
```

Output:

```
Good Luck
```

4. **while**

While a statement is true, it repeats.

Syntax: `(while <value 1> <value 2> <unlimited amount of values (optional>)`

Example:

```
(while (= 1 1) (print 1))
```

Output:

```
1
1
1
...
```

#### Error Functions

1. **raise**

Raises a SolarError.

Syntax: `(raise <value 1>)`

Example:

```
(raise "Hello, Bye, Good Luck")
```

Output:

```
Error raised: Hello, Bye, Good Luck
```

2. **datetime**

Returns the date and/or time.

Syntax: `(datetime <value 1 (optional)>)`

Example:

```
(print (datetime))
(print (datetime "a"))
```

Output (Note: These values are not the actual output, they are just an example as they vary):

```
Mon Dec 11 15:16:13 2018
Mon
```
For a complete list of the letters, see [03-datetime](/docs/03-datetime.md)

3. **random**

Returns a random number

Syntax: `(random <value 1 (optional)> <value 2 (optional)>)`

Example:

```
(print (random)) ` Between 0.0 and 1.0 `
(print (random 10)) `Between 0 and 10`
(print (random 3 10)) `Between 3 and 10`
```

Output:

```
0.4
6
4
```



- The Solar Team
