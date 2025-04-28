---
title: Program Flags
teaching: 5
exercises: 5
---

::::::::::::::::::::::::::::::::::::::: objectives

- Handle flags and files separately in a command-line program.

::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: questions

- How can I make an easy shortcut to analyze all files at once using a program flag?

::::::::::::::::::::::::::::::::::::::::::::::::::

## Handling Program Flags

Now we have a program which is capable of handling any number of data sets at once.

But what if we have 50 GDP data sets? It would be awfully tedious to type in the names
of 50 files in the command line, so let's add a flag to our program indicating that we
would like it to generate a plot for each data set in the current directory.

Flags are a convention used in programming to indicate to a program that a non-default behavior
is being requested by the user. In this case, we'll be using a "-a" flag to indicate to our program
we would like it to operate on all data sets in our directory.

To explore what files are in the current directory, we'll be using the Python's `glob` module.

- In Unix, the term "globbing" means "matching a set of files with a pattern".
- The most common patterns are:
  - `*` meaning "match zero or more characters"
  - `?` meaning "match exactly one character"
- Python contains the `glob` library to provide pattern matching functionality
- The `glob` library contains a function also called `glob` to match file patterns
- E.g., `glob.glob('*.txt')` matches all files in the current directory
  whose names end with `.txt`.
- Result is a (possibly empty) list of character strings.

<pre>
import sys
<b>import glob</b>
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

<b># check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
else:
    filenames = sys.argv[1:]

for filename in filenames:</b>

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

    # save the plot with a unique file name
    split_name1 = filename.split('.')[0] #data/gapminder_gdp_XXX
    split_name2 = filename.split('/')[1]
    save_name = 'figs/'+split_name2 + '.png'
    plt.savefig(save_name)
</pre>

Let's test if our run all flag works by running the script before we commit it.
It is always good pratice to run your code first so you don't accidently commit broken code.

```bash
python gdp_plots.py -a
```

```output
Traceback (most recent call last):
  File "gdp_plots.py", line 23, in <module>
    ax = data.plot(title = filename)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_core.py", line 1031, in __call__
    return plot_backend.plot(data, kind=kind, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_matplotlib/__init__.py", line 71, in plot
    plot_obj.generate()
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_matplotlib/core.py", line 451, in generate
    self._compute_plot_data()
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_matplotlib/core.py", line 636, in _compute_plot_data
    raise TypeError("no numeric data to plot")
TypeError: no numeric data to plot
```

This error is saying that the data in one or more of our files is non-numeric and it doesn't know how to plot it.
Lets add a little print statement to our code to check the head of our data file for each time through the loop.

<pre>
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
else:
    filenames = sys.argv[1:]

for filename in filenames:

    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(filename, index_col = 'country').T
    <b>print(filename)
    print(data.head())</b>

    # create a plot of the transposed data
    ax = data.plot(title = filename)

    # set some plot attributes
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Per Capita")
    # set the x locations and labels
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation = 45)

    # save the plot with a unique file name
    split_name1 = filename.split('.')[0] #data/gapminder_gdp_XXX
    split_name2 = filename.split('/')[1]
    save_name = 'figs/'+split_name2 + '.png'
    plt.savefig(save_name)
</pre>

Let's run the code again with our print statements

```bash
python gdp_plots.py -a
```

```output
data/gapminder_gdp_americas.csv
country           Argentina      Bolivia       Brazil  ... United States      Uruguay    Venezuela
continent          Americas     Americas     Americas  ...      Americas     Americas     Americas
gdpPercap_1952  5911.315053  2677.326347  2108.944355  ...   13990.48208  5716.766744  7689.799761
gdpPercap_1957  6856.856212  2127.686326  2487.365989  ...   14847.12712  6150.772969  9802.466526
gdpPercap_1962  7133.166023  2180.972546  3336.585802  ...   16173.14586  5603.357717  8422.974165
gdpPercap_1967  8052.953021  2586.886053  3429.864357  ...   19530.36557   5444.61962  9541.474188

[5 rows x 25 columns]
Traceback (most recent call last):
  File "gdp_plots.py", line 23, in <module>
    ax = data.plot(title = filename)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_core.py", line 1031, in __call__
    return plot_backend.plot(data, kind=kind, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_matplotlib/__init__.py", line 71, in plot
    plot_obj.generate()
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_matplotlib/core.py", line 451, in generate
    self._compute_plot_data()
  File "/opt/anaconda3/lib/python3.11/site-packages/pandas/plotting/_matplotlib/core.py", line 636, in _compute_plot_data
    raise TypeError("no numeric data to plot")
TypeError: no numeric data to plot
```

Now we can see in the America's gdp file there is a row of continent data. There was originally a continent column before we transposed it.
Because a we need the same type of data within each column, when we include a string row pandas converts all the values in that column into a string. So it isn't seeing any(!) of our number values as numeric data that can be plotted.

We can add a check into our code that drops the continent column if it exists. 

<pre>
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
else:
    filenames = sys.argv[1:]

for filename in filenames:

    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(filename, index_col = 'country').T
    <b>if "continent" in data.index:
        data.drop("continent", inplace=True)</b>
    print(filename)
    print(data.head())

    # create a plot of the transposed data
    ax = data.plot(title = filename)

    # set some plot attributes
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Per Capita")
    # set the x locations and labels
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation = 45)

    # save the plot with a unique file name
    split_name1 = filename.split('.')[0] #data/gapminder_gdp_XXX
    split_name2 = filename.split('/')[1]
    save_name = 'figs/'+split_name2 + '.png'
    plt.savefig(save_name)
</pre>

Now running the script again works!

```bash
python gdp_plots.py -a
```

It sill prints the filenames and head of each data frame though.  We should delete those lines and our final code should be the following script:

<pre>
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
else:
    filenames = sys.argv[1:]

for filename in filenames:

    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(filename, index_col = 'country').T
    if "continent" in data.index:
        data.drop("continent", inplace=True)

    # create a plot of the transposed data
    ax = data.plot(title = filename)

    # set some plot attributes
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP Per Capita")
    # set the x locations and labels
    ax.set_xticks(range(len(data.index)))
    ax.set_xticklabels(data.index, rotation = 45)

    # save the plot with a unique file name
    split_name1 = filename.split('.')[0] #data/gapminder_gdp_XXX
    split_name2 = filename.split('/')[1]
    save_name = 'figs/'+split_name2 + '.png'
    plt.savefig(save_name)
</pre>

### Updating the repository

Yet another successful update to the code. Let's
commit our changes.

```bash
$ git add gdp_plots.py
$ git commit -m "Adding a flag to run script for all gdp data sets."
```

:::::::::::::::::::::::::::::::::::::::::  callout

## The Right Way to Do It

If our programs can take complex parameters or multiple filenames,
we shouldn't handle `sys.argv` directly.
Instead,
we should use Python's `argparse` library,
which handles common cases in a systematic way,
and also makes it easy for us to provide sensible error messages for our users.
We will not cover this module in this lesson
but you can go to Tshepang Lekhonkhobe's [Argparse tutorial](https://docs.python.org/dev/howto/argparse.html)
that is part of Python's Official Documentation.


::::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::: keypoints

- Adding command line flags can be a user-friendly way to accomplish common tasks.

::::::::::::::::::::::::::::::::::::::::::::::::::


