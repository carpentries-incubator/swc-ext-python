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
