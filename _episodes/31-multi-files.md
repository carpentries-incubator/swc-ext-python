---
title: Trying Different Methods
teaching: 25
exercises: 2
questions:
- "How do I plot multiple files using different methods?"
objectives:
- "Read data from standard input in a program so that it can be used in a pipeline."
- "Compare using different methods to accomplish the same task."
- "Handle flags and files separately in a command-line program."
- "Practice making branches and merging in a Git repository."
keypoints:
- "Make different branches in a Git reposityory to try different methods."
- "Use bash's `time` command to time scripts."
---

## Handling Multiple Files

Perhaps we would like a script that can operate on multiple data files at
once. To process each file separately, we'll need a loop that executes our
plotting statements for each file.

We want our program to process each file separately, and the easiest way to do
this is a loop that executes once for each of the filenames provided in
`sys.argv`.

But we need to be careful: `sys.argv[0]` will always be the name of our program,
rather than the name of a file.  We also need to handle an unknown number of
filenames, since our program could be run for any number of files.

The solution is to loop over the contents of `sys.argv[1:]`. The '1' tells
Python to start the slice at location 1, so the program's name isn't included.
Since we've left off the upper bound, the slice runs to the end of the list, and
includes all the filenames.

Here is our updated program.

~~~
import sys
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

for filename in sys.argv[1:]:
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
~~~
{: .python}

Now when the program is given multiple filenames

~~~
$ python gdp_plots.py gapminder_gdp_oceania.csv gapminder_gdp_africa.csv
~~~
{: .bash}

one plot for each filename is generated.

#### Update the Repository

~~~
$ git add gdp_plots.py
$ git commit -m "Allowing plot generation for multiple files at once"
~~~
{: .bash}

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

    # display the plot
    plt.show()
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

> ## Finding Particular Files
>
> Using the `glob` module,
> write a simple version of `ls` that shows files in the current directory with a particular suffix.
> A call to this script should look like this:
>
> ~~~
> $ python my_ls.py py
> ~~~
> {: .python}
>
> ~~~
> left.py
> right.py
> zero.py
> ~~~
> {: .output}
>
> > ## Solution
> > ~~~
> > import sys
> > import glob
> >
> > def main():
> >     '''prints names of all files with sys.argv as suffix'''
> >     assert len(sys.argv) >= 2, 'Argument list cannot be empty'
> >     suffix = sys.argv[1] # NB: behaviour is not as you'd expect if sys.argv[1] is *
> >     glob_input = '*.' + suffix # construct the input
> >     glob_output = sorted(glob.glob(glob_input)) # call the glob function
> >     for item in glob_output: # print the output
> >         print(item)
> >     return
> >
> > main()
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}

> ## Counting Lines
>
> Write a program called `line_count.py` that works like the Unix `wc` command:
>
> *   If no filenames are given, it reports the number of lines in standard input.
> *   If one or more filenames are given, it reports the number of lines in each, followed by the total number of lines.
>
> > ## Solution
> > ~~~
> > import sys
> >
> > def main():
> >     '''print each input filename and the number of lines in it,
> >        and print the sum of the number of lines'''
> >     filenames = sys.argv[1:]
> >     sum_nlines = 0 #initialize counting variable
> >
> >     if len(filenames) == 0: # no filenames, just stdin
> >         sum_nlines = count_file_like(sys.stdin)
> >         print('stdin: %d' % sum_nlines)
> >     else:
> >         for f in filenames:
> >             n = count_file(f)
> >             print('%s %d' % (f, n))
> >             sum_nlines += n
> >         print('total: %d' % sum_nlines)
> >
> > def count_file(filename):
> >     '''count the number of lines in a file'''
> >     f = open(filename,'r')
> >     nlines = len(f.readlines())
> >     f.close()
> >     return(nlines)
> >
> > def count_file_like(file_like):
> >     '''count the number of lines in a file-like object (eg stdin)'''
> >     n = 0
> >     for line in file_like:
> >         n = n+1
> >     return n
> >
> > main()
> >
> > ~~~
> > {: .python}
> {: .solution}
{: .challenge}
