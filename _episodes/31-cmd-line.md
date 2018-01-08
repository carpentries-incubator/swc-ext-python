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

The Jupyter Notebook and other interactive tools are great for
prototyping code and exploring data, but sooner or later one will
want to use that code in a program we can run from the command line. 
In order to do that, we need to make our programs work like other
Unix command-line tools. For example, we may want a program that
reads a dataset and prints the average inflammation per patient.

> ## Switching to Shell Commands
>
> In this lesson we are switching from typing commands in a Python interpreter to typing
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
copy the text below into a file called `pandas_plots.py` and move
it into our working directory with the gapminder data (`~/data`).

~~~
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

# load data and transpose so that country names are
# the columns and their gdp data becomes the rows
data = pandas.read_csv('data/gapminder_gdp_oceania.csv', index_col = 'country').T

# create a plot the transposed data
ax = data.plot()
# display the plot
plt.show()
~~~
{: .python}

This program imports the `pandas` and `matplotlib` Python modules, reads
some of the gapminder data into a `pandas` dataframe, and plots that
data using `matplotlib` with some default settings.

We can run this program from the command line using `python pandas_plots.py`.
This is much easier than starting a notebook, going to the browser, and running
each cell in the notebook to get the same result.

This program currently only workd for one set of data. How might we modify
the program to work for any of the gapminder gdp datasets? We could go into the
script and change the `.csv` filename to generate the same plot for different
sets of data, but there is an even better way.

### Initialize a repository

But before we modify our `pandas_plots.py` program, we are going to put it under
version control so that we can track its changes as we go through this lesson.

~~~
$ git init
$ git add pandas_plots.sh
$ git commit -m "First commit of analysis script"
~~~
{: .bash}

Because we're only concerned with changes to our analysis script, we are going to
create a .gitignore file for all of the gapminder `.csv` files.

~~~
$ echo "*.csv" > .gitignore
$ git add .gitignore
$ git commit -m "Adding ignore file"
~~~

Now that we have a clean repository, let's get back to work on adding command line
arguments to our program.

## Command-Line Arguments

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
our current directory (a.k.a. the home directory) should do nicely

~~~
$ cd ..
$ pwd
~~~
{: .bash}

~~~
/home/swcuser
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

With this new information, we'll add command line arguments to our
`pandas_plots.py` program. Let's move back into our `~/data` directory

~~~
$ cd data
$ pwd
~~~
{: .bash}

~~~
/home/swcuser/data
~~~
{: .output}

To do this we'll make two changes, one is to add the import of the sys module at
the beginning of the program. The other is to replace the filename
("gapminder_gdp_oceania.csv") with the the second entry in the `sys.argv` list.

~~~
import sys
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

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

Now let's take a look at what happens when we provide a gapminder filename
to the program.

~~~
$ python pandas_plots.py ./data/gapminder_gdp_oceania.csv
~~~
{: .bash}

And the same plots as before were displayed, but this file is now being read
from an agrument we've provided on the command line. We can now do this for
files with similar information and get the same set of plots for that data
*without any changes to our program's code*. Try this our for yourself now.

### Updating our Repository

Now that we've made this change to our program and see that it works. Let's
update our repository with these changes.

~~~
$ git add pandas_plots.py
$ git commit -m "Adding command line arguments"
~~~
{: .bash}

### Returning Error Information

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
command and there is no entry in `sys.argv` where we're telling it to look for
this value. We may know all of this because we're the ones who wrote the
program, but another user of the program without this experience will not.

It is important to employ "defensive programming" in this scenario so that our
program indicates to the user **a)** what is going wrong and **b)** how to fix
this problem when running the program.

Let's add a section to the code which checks the number of incoming arguments to
the program and returns some information to the user.

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
Not enough arguments have been provided to the program.
Please provide a gapminder gdp data file to the program.
~~~
{: .python}

Now if someone runs this program without having used it before (or written it
themselves) the user will know how change their command to get the program
running properly, rather than seeing an esoteric Python error.

### Updating the Repo

We've just made successful change to our repository. Let's add a commit to the
repo.

~~~
$ git add pandas_plots.py
$ git commit -m "Handling case for missing filename argument"
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

## Handling Multiple Files

Perhaps we would like a script that can operate on multiple data files at
once. To process each file separately, we'll need a loop that executes our
plotting statements for each file.

We want our program to process each file separately, and the easiest way to do
this is a loop that executes once for each of the filenames provided in
`sys.argv`..

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

# make sure that a filename argument has been provided
if len(sys.argv) <= 1:
    # why the program will not continue
    print("Not enough arguments have been provided to the program.")
    # suggest what needs to be changed for a successful run 
    print("Please provide a gapminder gdp data file to the program.")
    # exit the program early
    sys.exit()

# loop over each filename
for file in sys.argv[1:]:
    # load data and transpose so that country names are
    # the columns and their gdp data becomes the rows
    data = pandas.read_csv(file, index_col = 'country').T
    # create a plot the transposed data
    ax = data.plot()
    # display the plots
    plt.show()
~~~
{: .python}

Now when the program is given multiple filenames

~~~
$ python pandas_plots.py gapminder_gdp_oceania.csv gapminder_gdp_africa.csv
~~~
{: .bash}

one plot for each filename is generated.

#### Update the Repository

~~~
$ git add pandas_plots.py
$ git commit -m "Allowing plot generation for multiple files at once"
~~~
{: .bash}

This code would look a lot nicer be easier to read if it were reorganized, and
we could use it in other Python programs to generate plots for our datasets.

This can be accomplished by making the argument checking section and the body of
the for loop their own functions. This requires surprisingly few changes to the
code.

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

Another thing we might want to do with this script is to import its ability to
generate plots in another place in Python. Let's see what happens if we try to
do that now.

First, let's open an interactive Python session in the terminal and import our
module.

~~~
$ python
>>> import pandas_plots
Not enough arguments have been provided to the program.
Please provide a gapminder gdp data file to the program.
$
~~~
{: .bash}

We see our error message related to a lack and the session is terminated. This
is a real problem if the functionality of the plot_datafile is needed
elsewhere. We could copy the function into another location of course, but then
if we change one of those functions the other will need to be updated as well
which is an unlikely scenario given the number of things on our plate
day-to-day.

> ## Running Versus Importing
>
> Running a Python script in bash is very similar to
> importing that file in Python.
> The biggest difference is that we don't expect anything
> to happen when we import a file,
> whereas when running a script, we expect to see some
> output printed to the console.
>
> In order for a Python script to work as expected
> when imported or when run as a script,
> we typically put the part of the script
> that produces output in the following if statement:
>
> ~~~
> if __name__ == '__main__':
>     main()  # Or whatever function produces output
> ~~~
> {: .python}
>
> When you import a Python file, `__name__` is the name
> of that file (e.g., when importing `pandas_plots.py`,
> `__name__` is `'pandas_plots'`). However, when running a
> script in bash, `__name__` is always set to `'__main__'`
> in that script so that you can determine if the file
> is being imported or run as a script.
{: .callout}

Let's add the main part of our script to a section which identifies the program
as being called from the command line.

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

if __name__ == "__main__":
   main()
~~~
{: .python}

Now if try to import this script from an interactive session and use our
function

~~~
$ python
>>> import pandas_plots
>>> pandas_plots.plot_datafile("gapminder_gdp_oceania.csv")
>>>
~~~
{: .bash}

the session doesn't terminate and we can use the `plot_datafile` function in an
interactive way. This would work the same way in a Jupyter notebook.

>> ## Exiting the Python interpreter
>> To exit the Python interpreter, use the key combination `ctrl+d`
>>
{: .callout}


## Handling Command-Line Flags

The next step is to teach our program to pay attention to the `--min`, `--mean`, and `--max` flags.
These always appear before the names of the files,
so we could just do this:

~~~
$ cat ../code/readings_04.py
~~~
{: .bash}

~~~
import sys
import numpy

def main():
    script = sys.argv[0]
        action = sys.argv[1]
	    filenames = sys.argv[2:]

    for f in filenames:
            data = numpy.loadtxt(f, delimiter=',')

        if action == '--min':
	            values = numpy.min(data, axis=1)
		            elif action == '--mean':
			                values = numpy.mean(data, axis=1)
					        elif action == '--max':
						            values = numpy.max(data, axis=1)

        for m in values:
	            print(m)

if __name__ == '__main__':
   main()
~~~
{: .python}

This works:

~~~
$ python ../code/readings_04.py --max small-01.csv
~~~
{: .bash}

~~~
1.0
2.0
~~~
{: .output}

but there are several things wrong with it:

1.  `main` is too large to read comfortably.

2. If we do not specify at least two additional arguments on the
   command-line, one for the **flag** and one for the **filename**, but only
      one, the program will not throw an exception but will run. It assumes that the file
         list is empty, as `sys.argv[1]` will be considered the `action`, even if it
	    is a filename. [Silent failures]({{ page.root }}/reference/#silence-failure)  like this
	       are always hard to debug.

3. The program should check if the submitted `action` is one of the three recognized flags.

This version pulls the processing of each file out of the loop into a function of its own.
It also checks that `action` is one of the allowed flags
before doing any processing,
so that the program fails fast:

~~~
$ cat ../code/readings_05.py
~~~
{: .bash}

~~~
import sys
import numpy

def main():
    script = sys.argv[0]
        action = sys.argv[1]
	    filenames = sys.argv[2:]
	        assert action in ['--min', '--mean', '--max'], \
		           'Action is not one of --min, --mean, or --max: ' + action
			       for f in filenames:
			               process(f, action)

def process(filename, action):
    data = numpy.loadtxt(filename, delimiter=',')

    if action == '--min':
            values = numpy.min(data, axis=1)
	        elif action == '--mean':
		        values = numpy.mean(data, axis=1)
			    elif action == '--max':
			            values = numpy.max(data, axis=1)

    for m in values:
            print(m)

if __name__ == '__main__':
   main()
   ~~~
   {: .python}

This is four lines longer than its predecessor,
but broken into more digestible chunks of 8 and 12 lines.

> ## Finding Particular Files
>
> Using the `glob` module introduced [earlier]({{ page.root }}/04-files/),
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
