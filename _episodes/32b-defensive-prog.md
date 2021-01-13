---
title: Defensive Programming
teaching: 10
exercises: 5
questions:
- "How do I predict and avoid user confusion?"
objectives:
- "Ensure that programs indicate use and provide meaningful output upon failure."
keypoints:
- "Avoid silent failures."
- "Avoid esoteric output when a program fails."
- "Add checkpoints in code to check for common failures."
---

## Defensive Programming

In our last lesson, we created a program which will plot our gapminder gdp data
for an arbitrary number of files. This is great, but we didn't cover some of
the vulnerabilities of this program we've created.

  - What happens if we run the program without any arguments at all?
  - What happens if we run the program from another directory?

First, let's try running our program without any additional arguments or flags.

~~~
$ python gdp_plots.py
~~~
{: .bash}

~~~
Traceback (most recent call last):
  File "gdp_plot.py", line 12, in <module>
    filenames = sys.argv[1:]
IndexError: list index out of range
~~~
{: .output}

Python returns an error when trying to find the command line argument in
`sys.argv`. It cannot find that argument because we haven't provided it to the
command and as a result there is no entry in `sys.argv` where we're telling it to look for
this value. We may know all of this because we're the ones who wrote the
program, but another user of the program without this experience will not.

> ## More on Function Errors/Exceptions
>
> Python reports a **runtime error** when something goes wrong while a program is executing.
>
> ~~~
> age = 53
> remaining = 100 - aege # mis-spelled 'age'
> ~~~
> {: .python}
>
> ~~~
> NameError: name 'aege' is not defined
> ~~~
> {: .error}
>
>  * The message indicates a problem with the name of a variable
>
> Python also reports a **syntax error** when it can't understand the source of a program.
>
> ~~~
> print("hello world"
> ~~~
> {: .python}
>
> ~~~
>   File "<ipython-input-6-d1cc229bf815>", line 1
>     print ("hello world"
>                         ^
> SyntaxError: unexpected EOF while parsing
> ~~~
> {: .error}
>
> *   The message indicates a problem on first line of the input ("line 1").
>     *   In this case the "ipython-input" section of the file name tells us that
>         we are working with input into IPython,
>         the Python interpreter used by the Jupyter Notebook.
> *   The `-6-` part of the filename indicates that
>     the error occurred in cell 6 of our Notebook.
> *   Next is the problematic line of code,
>     indicating the problem with a `^` pointer.
>
{: .callout}

And if we run the program from another directory:

~~~
$ cd ..
$ python swc-gapminder/gdp_plots.py -a
~~~
{: .bash}

We see no output from the program at all. This is what is referred to as a "silent
failure". The program has failed to produce a plot, but has reported no reason why.
These kind of failures are difficult to debug and should be avoided.

It is important to employ "defensive programming" in this scenario so that our
program indicates to the user

 1. what is going wrong
 2. how to correct this problem

### Check Input Arguments

Let's add a section to the code which checks the number of incoming arguments to
the program and returns some information to the user if there is missing information.

<pre>
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# make sure additional arguments or flags have
# been provided by the user
<b>if len(sys.argv) == 1:
    # why the program will not continue
    print("Not enough arguments have been provided")
    # how this can be corrected
    print("Usage: python gdp_plots.py < filenames >")
    print("Options:")
    print("-a : plot all gdp data sets in current directory")
    exit()</b>

# check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
else:
    filenames = sys.argv[1:]

for filename in filenames:

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
    split_name2 = split_name1.split('/')[1]
    save_name = 'figs/'+split_name2 + '.png'
    plt.savefig(save_name)
</pre>
{: .python}

If we run the program without a filename argument, here's what we'll see

~~~
$ python gdp_plots.py
~~~
{: .python}

~~~
Not enough arguments have been provided
Usage: python gdp_plots.py <filenames>
Options:
-a : plot all gdp file in current directory
~~~
{: .output}

Now if someone runs this program without having used it before (or written it
themselves) the user will know how change their command to get the program
running properly, rather than seeing an esoteric Python error.

### Update the Repository

We've just made another successful change to our repository. Let's add a commit
to the repo.

~~~
$ git add gdp_plots.py
$ git commit -m "Handling case for missing filename argument"
~~~
{: .bash}

### Check for silent errors

Silent errors can be difficult to anticipate. If we try to run our program
from another directory with the `-a` flag, we don't see any errors, but it
also doesn't do anything. This is because when we do the `-a` flag here,
there are no `.csv` files in the directory, so our `filenames` variable is
empty. Let's add a check to ensure there are files to plot.

<pre>
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# make sure additional arguments or flags have
# been provided by the user
if len(sys.argv) == 1:
    # why the program will not continue
    print("Not enough arguments have been provided")
    # how this can be corrected
    print("Usage: python gdp_plots.py < filenames >")
    print("Options:")
    print("-a : plot all gdp data sets in current directory")
    exit()

# check for -a flag in arguments
if "-a" in sys.argv:
    filenames = glob.glob("data/*gdp*.csv")
    # check if no files were found and print message.
    <b>if filenames == []:
        # file list is empty (no files found)
        print("No files found in this folder.")
        print("Make sure data is located in current directory.")
        exit()</b>
else:
    filenames = sys.argv[1:]

for filename in filenames:

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
    split_name2 = split_name1.split('/')[1]
    save_name = 'figs/'+split_name2 + '.png'
    plt.savefig(save_name)
</pre>
{: .python}

Now if someone runs this program in a directory with no valid datafiles,
a message appears.

### Update the Repository

We've just made another successful change to our repository. Let's add a commit
to the repo.

~~~
$ git add gdp_plots.py
$ git commit -m "Handling case if no files present in directory"
~~~
{: .bash}
