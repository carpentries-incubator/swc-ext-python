---
title: Refactoring
teaching: 10
exercises: 1
questions:
- "When should I reorganize my code so it is more clear and readable for others?"
- "How can I organize my code so that it is useable in other places?"
- "Why do I almost always want to write my code as though it will be used somewhere else?"
objectives:
- "Understand the value of refactoring code and use of functions."
keypoints:
- "Refactoring makes code more modular, easier to read, and easier to understand."
- "Refactoring requires one to consdier future implications and generally enables
   others to use your code more easily."
---

This code works nicely for generating plots of multiple data sets, but there is
now a lot of code to digest in our script. Picture yourself looking at this code for
the first time. Would it be immediately clear to you where are arguments are handled
and where plots are generated?

It would be nice to break this work into clear chunks of code. This can be
accomplished by making the argument checking section and the body of the for
loop their own functions. This requires surprisingly few changes to the code, 
but makes it much more clear. This process is called **refactoring**.. 

### Create a Branch

Before we set to work, let's make a new branch to work in.

~~~
$ git checkout -b refactor
~~~
{: .bash}

Once this is complete, our program now looks something like this:

~~~
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

"""
Parse the argument list and return a list
of filenames.
"""
def parse_arguments():
    # make sure additional arguments or flags have
    # been provided by the user
    if len(sys.argv) == 1:
        # why the program will not continue
        print("Not enough arguments have been provided")
        # how this can be corrected
        print("Usage: python gdp_plots.py <filenames>")
        print("Options:")
        print("-a : plot all gdp data sets in current directory")

    # check for -a flag in arguments
    if "-a" in sys.argv:
        filenames = glob.glob("*gdp*.csv")
    else:
        filenames = sys.argv[1:]

    return filenames

"""
Takes in a list of filenames to plot
and creates a plot for each file.
"""
def create_plots(filenames):
    for filename in filenames:
        # read data into a pandas dataframe and transpose
        data = pandas.read_csv(filename, index_col = 'country').T

        # create a plot the transposed data
        ax = data.plot( title = filename )

        # set some plot attributes
        ax.set_xlabel("Year")
        ax.set_ylabel("GDP Per Capita")
        # set the x locations and labels
        ax.set_xticks( range(len(data.index)) )
        ax.set_xticklabels( data.index, rotation = 45 )
        
        # display the plot
        plt.show()

"""
 main function - does all the work        
"""
def main():
    # parse arguments
    files_to_plot = parse_arguments()

    #generate plots
    create_plots(files_to_plot)

# call main
main()
~~~
{: .python}

The behavior of the program hasn't changed, but it has been made more modular by
separating the into different functions with their own purpose. 

#### Update the Repository

We haven't changed the behavior of our program, but our *code* has changed, so
let's update the repository.

~~~
$ git add pandas_plots.py
$ git commit -m "Reorganizing code."
~~~
{: .bash}

> ## Branching and Refactoring
>
> To demonstrate that the behavior of our program hasn't changed,
> try running it a few different ways using both the `master` and
> `refactor` branches. Remember that the command for checking out
> a branch is `git checkout <branch_name>`.
>
{: .challenge}

