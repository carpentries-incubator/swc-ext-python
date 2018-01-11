---
title: Command-Line Programs
teaching: 45
exercises: 2
questions:
- "How can I write Python programs that will work like Unix command-line tools?"
objectives:
- "Use the values of command-line arguments in a program."
- "Handle flags and files separately in a command-line program."
- "Read data from standard input in a program so that it can be used in a pipeline."
keypoints:
- "The `sys` library connects a Python program to the system it is running on."
---

The Jupyter Notebook and other interactive tools are great for
prototyping code and exploring data, but sooner or later one will
want to use that code in a program we can run from the command line. 
In order to do that, we need to make our programs work like other
Unix command-line tools. For example, we may want a program that
reads a gapminder data set and plots the gdp of countries over time.

> ## Switching to Shell Commands
>
> In this lesson we are switching from typing commands in Jupyter notebooks to typing
> commands in a shell terminal window (such as bash). When you see a `$` in front of a
> command that tells you to run that command in the shell rather than the Python interpreter.
{: .callout}

> ## Converting Notebooks
>
> The Jupyter Notebook has the ability to convert all of the cells of a
> current Notebook into a python program. To do this, go to `File` -> `Download as`
> and select `Python (.py)` to get the current notebook as a Python script.
> 
{: .callout}

To ensure that we're all starting with the same set of code. Please
copy the text below into a file called `gdp_plots.py` in our working directory
with the gapminder data (`~/Desktop/data`). Alternatively, you can [download the file
here](http://christinalk.github.io/python-novice-gapminder-custom/scripts/gdp_plots.py) and move it the `~/Desktop/data` directory.

~~~
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows

# read data into a pandas dataframe and transpose
data = pandas.read_csv('gapminder_gdp_oceania.csv', index_col = 'country').T

# create a plot the transposed data
ax = data.plot()

# display the plot
plt.show()
~~~
{: .python}

This program imports the `pandas` and `matplotlib` Python modules, reads
some of the gapminder data into a `pandas` dataframe, and plots that
data using `matplotlib` with some default settings.

We can run this program from the command line using

~~~
$ python gdp_plots.py
~~~
{: .bash}

This is much easier than starting a notebook, going to the browser, and running
each cell in the notebook to get the same result.


### Initialize a repository

But before we modify our `gdp_plots.py` program, we are going to put it under
version control so that we can track its changes as we go through this lesson.

~~~
$ git init
$ git add gdp_plots.sh
$ git commit -m "First commit of analysis script"
~~~
{: .bash}

Because we're only concerned with changes to our analysis script, we are going to
create a .gitignore file for all of the gapminder `.csv` files and any Python notebook
files (`.ipynb`) files we have created thus far.

~~~
$ echo "*.csv" > .gitignore
$ echo "*.ipynb" >> .gitignore
$ git add .gitignore
$ git commit -m "Adding ignore file"
~~~

Now that we have a clean repository, let's get back to work on adding command line
arguments to our program.

## Changing code under Version Control

As it is, this plot isn't bad but let's add some labels for clarity. We'll use the
data filename as a title for the plot and indicate what information in on each axis.

~~~
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

filename = 'gapminder_gdp_oceania.csv'

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

Now when we run this, our plot looks a little bit nicer.

~~~
$ python gdp_plots.py
~~~
{: .bash}

### Updating the Repository

~~~
$ git add gdp_plots.py
$ git commit -m "Improving plot format"
~~~
{: .bash}

## Command-Line Arguments

This program currently only works for the Oceania set of data. How might we modify
the program to work for any of the gapminder gdp data sets? We could go into the
script and change the `.csv` filename to generate the same plot for different
sets of data, but there is an even better way.

Python programs can use additional arguments provided in the following manner.

~~~
$ python <program> <argument1> <argument2> <other_arguments>
~~~
{: .bash}

The program can then use these arguments to alter its behavior based on those arguments.
In this case, we'll be using arguments to tell our program to operate on a specific file.

We'll be using the `sys` module to do so. `sys` (short for system) is a standard
Python module used to store information about the program and its running
environment, including what arguments were passed to the program when the
command was executed. These arguments are stored as a list in `sys.argv`.

These arguments can be accessed in our program by importing the `sys`
module. The first argument in `sys.argv` is always the name of the program, so
we'll find any additional arguments right after that in the list.

Let's try this out in a separate location on your machine. The directory above
our current directory should do nicely

~~~
$ cd ..
$ pwd
~~~
{: .bash}

~~~
/home/swcuser/Desktop/data/
~~~
{: .output}

Using the text editor of your choice, let's write a new program called
`args_list.py` containing the two following lines:

~~~
import sys
print('sys.argv is', sys.argv)
~~~
{: .python}

The strange name `argv` stands for "argument values".  Whenever Python runs a
program, it takes all of the values given on the command line and puts them in
the list `sys.argv` so that the program can determine what they were.  If we run
this program with no arguments:

~~~
$ python argv_list.py
~~~
{: .bash}

~~~
sys.argv is ['argv_list.py']
~~~
{: .output}

the only thing in the list is the full path to our script,
which is always `sys.argv[0]`.

If we run it with a few arguments, however:

~~~
$ python argv_list.py first second third
~~~
{: .bash}

~~~
sys.argv is ['argv_list.py', 'first', 'second', 'third']
~~~
{: .output}

then Python adds each of those arguments to that magic list.

Using this new information, let's add command line arguments to our
`gdp_plots.py` program.

First, we need to move back into our `~/data` directory

~~~
$ cd data
$ pwd
~~~
{: .bash}

~~~
/home/swcuser/Desktop/data
~~~
{: .output}

To do this we'll make two changes, one is to add the import of the sys module at
the beginning of the program. The other is to replace the filename
("gapminder_gdp_oceania.csv") with the the second entry in the `sys.argv` list.

Now our program should look as follows:

~~~
import sys
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

filename = sys.argv[1]

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

Let's take a look at what happens when we provide a gapminder filename
to the program.

~~~
$ python gdp_plots.py gapminder_gdp_oceania.csv
~~~
{: .bash}

And the same plot as before is displayed, but this file is now being read
from an agrument we've provided on the command line. We can now do this for
files with similar information and get the same set of plots for that data
*without any changes to our program's code*. Try this our for yourself now.

### Update the Repository

Now that we've made this change to our program and see that it works. Let's
update our repository with these changes.

~~~
$ git add gdp_plots.py
$ git commit -m "Adding command line arguments"
~~~
{: .bash}

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
