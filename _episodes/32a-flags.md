---
title: Program Flags
teaching: 5
exercises: 0
questions:
- "How do I plot multiple files using different methods?"
objectives:
- "Read data from standard input in a program so that it can be used in a pipeline."
- "Compare using different methods to accomplish the same task."
- "Handle flags and files separately in a command-line program."
- "Practice making branches and merging in a Git repository."
keypoints:
- "Make different branches in a Git repository to try different methods."
- "Use bash's `time` command to time scripts."
---

## Handling Program Flags

Now we have a program which is capable of handling any number of data sets at once.

But what if we have 50 GDP data sets? It would be awfully tedious to type in the names
of 50 files in the command line, so let's add a flag to our program indicating that we
would like it to generate a plot for each data set in the current directory.

Flags are a convention used in programming to indicate to a program that a non-default behavior
is being requested by the user. In this case, we'll be using a "-a" flag to indicate to our program
we would like it to operate on all data sets in our directory.

To explore what files are in the current directory, we'll be using the Python's `glob` module.

*   In Unix, the term "globbing" means "matching a set of files with a pattern".
*   The most common patterns are:
    *   `*` meaning "match zero or more characters"
    *   `?` meaning "match exactly one character"
*   Python contains the `glob` library to provide pattern matching functionality
*   The `glob` library contains a function also called `glob` to match file patterns
*   E.g., `glob.glob('*.txt')` matches all files in the current directory
    whose names end with `.txt`.
*   Result is a (possibly empty) list of character strings.

~~~
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("*gdp*.csv")
else:
    filenames = sys.argv[1:]

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

    # save the plot with a unique file name
    save_name = filename.split('.')[0] + '.png'
    plt.savefig(save_name)
~~~
{: .python}

### Updating the repository

Yet another successful update to the code. Let's
commit our changes.

~~~
$ git add gdp_plots.py
$ git commit -m "Adding a flag to run script for all gdp data sets."
~~~
{: .bash}


> ## The Right Way to Do It
>
> If our programs can take complex parameters or multiple filenames,
> we shouldn't handle `sys.argv` directly.
> Instead,
> we should use Python's `argparse` library,
> which handles common cases in a systematic way,
> and also makes it easy for us to provide sensible error messages for our users.
> We will not cover this module in this lesson
> but you can go to Tshepang Lekhonkhobe's [Argparse tutorial](http://docs.python.org/dev/howto/argparse.html)
> that is part of Python's Official Documentation.
{: .callout}
