---
title: Command-Line Programs
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


This code works nicely for generating plots of multiple data sets, but there is
now a lot of code to digest in our script. It would be nice to break this work
into clear chunks of code. This can be accomplished by making the argument
checking section and the body of the for loop their own functions. This requires
surprisingly few changes to the code.

~~~
import sys
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

def check_arguments():
    if len(sys.argv) <= 1:
        # why the program will not continue
        print("Not enough arguments have been provided to the program.")
        # suggest what needs to be changed for a successful run 
        print("Please provide a gapminder gdp data file to the program.")
        # exit the program early
        sys.exit()

def plot_datafile(filename):
    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(filename, index_col = 'country').T
    # create a plot the transposed data
    ax = data.plot()
    # display the plots
    plt.show()

def main():
    # make sure that a filename argument has been provided
    check_arguments()

    # loop over each filename
    for filename in sys.argv[1:]:
        plot_datafile(filename)

main()
~~~
{: .python}

The process we've just gone through is called **refactoring**. The behavior of
the program hasn't changed, but it has been made more modular by separating the
into different functions with their own purpose. These functions can then be
called within a function named "main" to execute the program.

#### Update the Repository

We haven't changed the behavior of our program, but our *code* has changed, so
let's update the repository.

~~~
$ git add pandas_plots.py
$ git commit -m "Reorganizing code."
~~~
{: .bash}
