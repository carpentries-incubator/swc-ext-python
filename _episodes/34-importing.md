---
title: Running Scripts and Importing
teaching: 30
exercises: 0
questions:
- "How can I import some of my work even if it is part of a program?"
objectives:
- "Learn how to import functions from one script into another."
- "Understand the difference between using a file as a module and running it as a script or program."
keypoints:
- "The `__name__` variable allows us to know whether the file is being imported or run as a script."
---

In our last lesson we learned how refactoring code makes it easier to understand
organize into pices that each have their own purpose. The added modularity also makes
it easier to use in other places.

First, let's start a Jupyter notebook in our current directory
and see what happens if we try to import our file as it is.

~~~
import gdp_plots
~~~
{: .python}

The result is an error related to how Python is attempting to interpret
the file. This is because Python is encountering our call to the function
`main` and isn't sure how to proceed.

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

Let's add the main function in our script to a section which identifies the program
as being called from the command line.

~~~
import sys
import glob
import pandas
# we need to import part of matplotlib
# because we are no longer in a notebook
import matplotlib.pyplot as plt

def parse_arguments():
    """
    Parse the argument list and return a list
    of filenames.
    """
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

def create_plot(filename):
    """
    Creates a plot for the specified
    data file.
    """
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

def create_plots(filenames):
    """
    Takes in a list of filenames to plot
    and creates a plot for each file.
    """
    for filename in filenames:
        create_plot(filename)

def main():
    """
    main function - does all the work        
    """
    # parse arguments
    files_to_plot = parse_arguments()

    #generate plots
    create_plots(files_to_plot)

if __name__ == "__main__":
    # call main
    main()
~~~
{: .python}

Now let's go back to the Jupyter notebook and try importing the file again

~~~
import gdp_plots
~~~
{: .python}

Success! You've just writeen your first Python module. Any of the functions in that module can now be accessed in our Jupyter notebook session.

~~~
%matplotlib inline
gdp_plots.create_plot("gapminder_gdp_oceania.csv")
~~~
{: .python}

### Update the repository

Back in the terminal, let's commit these changes to our repository.

~~~
$ git add gdp_plots.py
$ git commit -m "Moving call to the main function."
~~~
{: .bash}

> ## Writing Modular Code
> In our previous lesson we refactored our code for clarity and modularity.
> As part of that process we created two functions `create_plot` and `create_plots`.
> While the `create_plot` function wasn't used in our program, imagine importing our
> module and finding that the only way to generate a plot for a single file
> is to add that filename to a list before passing that list to `create_plots`.
>
> This might seem very strange or confusing to someone importing our module
> for the first time. It take time to develop an intuition for design decisions like
> these, but here are a few questions to ask yourself as a guide when organizing code: 
>
>   - Are my functions able to stand on their own? Do they accomplish simple tasks?
>   - Is it easy to write a clear function names in my module?
>     A function with the name "create_plots_and_export_data" is likely better
>     off being borken up into two functions "create_plots" and "export_data"
>   - Are my function names plural?
>      In our example, it may have felt more natural to create only one function,
>      "create_plots". In these cases, it is almost always useful to create a
>      function which does our operation once ("create_plot") and another plural
>      form of the function ("create_plots") which contains a loop over the
>      singular function.
>
{: .callout}