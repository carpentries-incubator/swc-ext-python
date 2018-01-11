---
title: "Function Errors"
teaching: 10
exercises: 10
questions:
- "What kind of errors can occur in programs?"
objectives:
- "Correctly describe situations in which SyntaxError and NameError occur."
keypoints:
- "Python reports a syntax error when it can't understand the source of a program."
- "Python reports a runtime error when something goes wrong while a program is executing."
- "Fix syntax errors by reading the source code, and runtime errors by tracing the program's execution."
---


## Python reports a syntax error when it can't understand the source of a program.

*   Won't even try to run the program if it can't be parsed.

~~~
# Forgot to close the quotation marks around the string.
name = 'Feng
~~~
{: .python}
~~~
SyntaxError: EOL while scanning string literal
~~~
{: .error}

~~~
# An extra '=' in the assignment.
age = = 52
~~~
{: .python}
~~~
SyntaxError: invalid syntax
~~~
{: .error}

*   Look more closely at the error message:

~~~
print("hello world"
~~~
{: .python}
~~~
  File "<ipython-input-6-d1cc229bf815>", line 1
    print ("hello world"
                        ^
SyntaxError: unexpected EOF while parsing
~~~
{: .error}

*   The message indicates a problem on first line of the input ("line 1").
    *   In this case the "ipython-input" section of the file name tells us that
        we are working with input into IPython,
        the Python interpreter used by the Jupyter Notebook.
*   The `-6-` part of the filename indicates that
    the error occurred in cell 6 of our Notebook.
*   Next is the problematic line of code,
    indicating the problem with a `^` pointer.

## Python reports a runtime error when something goes wrong while a program is executing.

~~~
age = 53
remaining = 100 - aege # mis-spelled 'age'
~~~
{: .python}
~~~
NameError: name 'aege' is not defined
~~~
{: .error}

*   Fix syntax errors by reading the source and runtime errors by tracing execution.
