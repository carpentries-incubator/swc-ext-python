---
title: Command-Line Programs
teaching: 15
exercises: 15
questions:
- "How can I write Python programs that will work like Unix command-line tools?"
objectives:
- "Use the values of command-line arguments in a program."
- "Read data from standard input in a program so that it can be used in a pipeline."
keypoints:
- "The `sys` library connects a Python program to the system it is running on."
- "The variable `sys.argv` is a list with each item being a command-line argument."
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

## Setting up your project

Up until now, we've been working in the data folder directly. Because we're going to be dealing with more files
of different types in this lesson, let's do a little rearranging: 

* On your desktop, create a folder called `swc-gapminder`. 
* Move the `data` folder you've been using into this folder.
* Inside swc-gapminder, create a folder called `figs`
* To ensure that we're all starting with the same set of code, copy the text below 
into a file called `gdp_plots.py` in the `swc-gapminder` folder or 
download the file from (here)[https://uw-madison-datascience.github.io/python-novice-gapminder-custom/scripts/gdp_plots.py].

~~~
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country').T

# create a plot of the transposed data
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
$ git add gdp_plots.py
$ git commit -m "First commit of analysis script"
~~~
{: .bash}

Because we're only concerned with changes to our analysis script, we are going to
create a .gitignore file for all of the gapminder `.csv` files and any Python notebook
files (`.ipynb`) files we have created thus far.

~~~
$ echo "data/*.csv" > .gitignore
$ echo "*.ipynb" >> .gitignore
$ git add .gitignore
$ git commit -m "Adding ignore file"
~~~

Now that we have a clean repository, let's get back to work on adding command line
arguments to our program.

## Changing code under Version Control

As it is, this plot isn't bad but let's add some labels for clarity. We'll use the
data filename as a title for the plot and indicate what information is in on each axis.

~~~
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

filename = 'data/gapminder_gdp_oceania.csv'

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv(filename, index_col = 'country').T

# create a plot of the transposed data
ax = data.plot(title = filename)

# set some plot attributes
ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Capita")
# set the x locations and labels
ax.set_xticks(range(len(data.index)))
ax.set_xticklabels(data.index, rotation = 45)

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

Let's try this out in a separate script. Using the text editor of your choice, let's write 
a new program called `args_list.py` containing the two following lines:

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

To do this, we'll make two changes:
1. add the import of the sys module at the beginning of the program. 
2. replace the filename ("data/gapminder_gdp_oceania.csv") with the the second entry in the 
`sys.argv` list.

Now our program should look as follows:

<pre>
<b>import sys</b>
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

<b>filename = sys.argv[1]</b>

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv(filename, index_col = 'country').T

# create a plot of the transposed data
ax = data.plot(title = filename)

# set some plot attributes
ax.set_xlabel("Year")
ax.set_ylabel("GDP Per Capita")
# set the x locations and labels
ax.set_xticks(range(len(data.index)) )
ax.set_xticklabels(data.index, rotation = 45)

# display the plot
plt.show()
</pre>
{: .python}

Let's take a look at what happens when we provide a gapminder filename
to the program.

~~~
$ python gdp_plots.py data/gapminder_gdp_oceania.csv
~~~
{: .bash}

And the same plot as before is displayed, but this file is now being read
from an argument we've provided on the command line. We can now do this for
files with similar information and get the same set of plots for that data
*without any changes to our program's code*. Try this our for yourself now.

### Update the Repository

Now that we've made this change to our program and see that it works. Let's
update our repository with these changes.

~~~
$ git add gdp_plots.py
$ git commit -m "Adding command line arguments"
~~~

> ## Exercise: read multiple files
> Try to run the gdp_plot.py so that it reads in all the .csv files in the data folder 
> using the wildcard symbol. Does it work? Why or why not?
> > ## Solution
> > 
> > if you run it with the argument 'data/*.csv' you get an error on the Americas file because it has an extra file.
> > However, it works if you omit that file.
> {: .solution}
{: .challenge}
