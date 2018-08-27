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
once. This can actually be done in two different ways: (1) writing a
bash script that calls our already-existing Python script in a for-loop, or
(2) modifying our Python script to read multiple files in a for-loop.
We will try both methods and compare the two.

### Create New Branches

First we will create two new branches where we can develop each of these
two different methods. We will call these branches `python-multi-files` and
`bash-multi-files`

~~~
$ git branch python-multi-files
$ git branch bash-multi-files
~~~
{: .bash}

We can check that these two branches were created with `$ git branch -a`.

## Handling Multiple Files with Python

First, we'll try using just Python to loop through mutliple files. Let's
switch to Python branch.

~~~
$ git checkout python-multi-files
~~~
{: .bash}

To process each file separately, we'll need a loop that executes our
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


## Saving Figures

By using `plt.show()` with multiple files, the program stops each
time a figure is generated and the user must exit it to continue.
To avoid this slow down, we can replace this with `plt.savefig()` and
view all the figures after the script finishes. This function has one
required argument which is the filename to save the figure as. The filename
must have a valid image extension (eg. PNG, JPEG, etc.).

Let's replace our `plt.show()` with `plt.savefig('gdp-plot.png)`. Our
new script should like like this:

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

    # save the plot
    plt.savefig('gdp-plot.png')
~~~
{: .python}

If we look at the contents of our folder now, we should have a new
file called `gdp-plot.png`. But why is there only one when we supplied
multiple data files? This is because each time the plot is created,
it is being saved as the same file name and overwriting the previous
plot.

We can fix this by creating a unique file name each time. A simple
unique name can be used based on the original file name. We can use
Python's `split()` function to split `filename`, which is a string,
by any character. This returns a list like so:

~~~
name = 'my-data.csv'
split_name = name.split('.')
print(split_name)
print(split_name[0])
~~~
{: .python}

~~~
['my-data', 'csv']
'my-data'
~~~

We'll split the original file name and use the first part to rename
our plot. And then we will concatenate `.png` to the name to specify
our file type.

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
$ git commit -m "Saves each figure as a separate file."
~~~
{: .bash}

## More Practice

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
