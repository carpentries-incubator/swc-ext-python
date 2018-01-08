---
title: Refactoring Code
teaching: 30
exercises: 0
questions:
- "How can I write Python programs that will work like Unix command-line tools?"
objectives:
- "Use the values of command-line arguments in a program."
- "Handle flags and files separately in a command-line program."
- "Read data from standard input in a program so that it can be used in a pipeline."
keypoints:
- "The `sys` library connects a Python program to the system it is running on."
- "The list `sys.argv` contains the command-line arguments that a program was run with."
- "Avoid silent failures."
- "The pseudo-file `sys.stdin` connects to a program's standard input."
- "The pseudo-file `sys.stdout` connects to a program's standard output."
---


## Defensive Programming

Having the ability to run our program on any of the gapminder gdp data sets is
great, but what happens if we run the code as we did before the addition of
arguments?

~~~
$ python pandas_plots.py
~~~
{: .bash}

~~~
Traceback (most recent call last):
  File "pandas_analysis1.py", line 9, in <module>
    data = pandas.read_csv(sys.argv[1], index_col = 'country').T
IndexError: list index out of range
~~~
{: .output}

Python returns an error when trying to find the command line argument in
`sys.argv`. It cannot find that argument because we haven't provided it to the
command and as a result there is no entry in `sys.argv` where we're telling it to look for
this value. We may know all of this because we're the ones who wrote the
program, but another user of the program without this experience will not.

It is important to employ "defensive programming" in this scenario so that our
program indicates to the user

 1. what is going wrong
 2. how to fix this problem

Let's add a section to the code which checks the number of incoming arguments to
the program and returns some information to the user if there is missing information.

~~~
import sys
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# make sure that a filename argument has been provided
if len(sys.argv) <= 1:
    # why the program will not continue
    print("Not enough arguments have been provided to the program.")
    # suggest what needs to be changed for a successful run 
    print("Please provide a gapminder gdp data file to the program.")
    # exit the program early
    sys.exit()

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv(sys.argv[1], index_col = 'country').T
print(data)
# create a plot the transposed data
ax = data.plot()
# display the plot
plt.show()
~~~
{: .python}

If we run the program without a filename argument, here's what we'll see

~~~
$ python pandas_plots.py
~~~
{: .python}

~~~
Not enough arguments have been provided to the program.
Please provide a gapminder gdp data file to the program.
~~~
{: .output}

Now if someone runs this program without having used it before (or written it
themselves) the user will know how change their command to get the program
running properly, rather than seeing an esoteric Python error.

### Update the Repository

We've just made another successful change to our repository. Let's add a commit
to the repo.

~~~
$ git add pandas_plots.py
$ git commit -m "Handling case for missing filename argument"
~~~
{: .bash}
