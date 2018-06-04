---
title: "Review Exercise"
teaching: 0
exercises: 20
questions:
- "How can we put together all of yesterday's material?"
objectives:
- "Apply use of functions, conditionals and loops to solve a problem."
keypoints:
- "Use skills together."
---

> ## Review From Yesterday
>
> In your notebook, write a function that determines whether a year between 1901 and 2000 is a leap year,
> where it prints a message like "1904 is a leap year" or "1905 is not a leap year" as
> output.  Use this function to evaluate the years 1928, 1950, 1959, 1972 and 1990.
> Essentially, given this list of years:
> ~~~~
> years = [1928, 1950, 1959, 1972, 1990]
> ~~~~
> {: .python}
>
> Produce something like:
>
> ~~~
> 1928 is a leap year
> 1950 is not a leap year.
> 1959 is not a leap year.
> 1972 is a leap year
> 1990 is not a leap year.
> ~~~
> {: .output
>
> Hint: the percent symbol '%' is the modular operator in Python.  So:
>
> ~~~
> print('8 mod 4 equals', 8 % 4)
> print('10 mod 4 equals', 10 % 4)
> ~~~
> {: .python}
> ~~~
> 8 mod 4 equals 0
> 10 mod 4 equals 2
> ~~~
> {: .output}
>
> If you're not sure where to start, see the partial answers below:
>
> > ## Suggested Approach
> >
> > First, try to determine how to use the mod operator `%` to determine
> > if a year is divisible by 4 (and thus a leap year or not).
> >
> > Then, create a conditional statement to use this information, and put
> > it into a function.
> >
> > Finally, create a list of the years given in the exercise.  Use a for loop
> > and your function to evaluate these years.
> >
> {: .solution}
>
> > ## Modular Arthimetic
> >
> > If a year in the range specified is divisible by four, it is a leap year.
> > If a number is divisible by 4, then the arithmetic expression "number mod four" (or
> > `num % 4` in Python) will equal zero.
> >
> {: .solution}
>
> > ## Conditional Statement
> >
> > Fill in the blanks:
> >
> > ~~~
> > year = 1904
> > if year % 4 == _____:
> >     print(year, _______________)
> > ______:
> >     print(year, "is not a leap year.")
> > ~~~
> > {: .python}
> >
> {: .solution}
>
> > ## Function
> >
> > Fill in the blanks:
> >
> > ~~~
> > def leap_year(year):
> >     _________
> > ~~~
> > {: .python}
> >
> {: .solution}
>
> > ## Loop
> >
> > Fill in the blanks:
> >
> > ~~~
> > year_list = [1928, 1950, 1959, 1972, 1990]
> > for year in ______:
> >     ________(year)
> > ~~~
> > {: .python}
> >
> {: .solution}
>
> > ## Complete Solution
> >
> > ~~~
> > def leap_year(year):
> >     if year % 4 == 0:
> >         print(year, "is a leap year")
> >     else:
> >         print(year, "is not a leap year.")
> >
> > year_list = [1928, 1950, 1959, 1972, 1990]
> > for year in year_list:
> >     leap_year(year)
> > ~~~
> > {: .python}
> >
> {: .solution}
>
> If you have time:
>
> 1. Expand your function so that it correctly categorizes
> any year from 0 onwards
>
> 1. Instead of printing whether a year is a leap year or not, save
> the results to a python dictionary, where there are two keys ("leap"
> and "not-leap") and the values are a list of years.
>
{: .challenge}

[anaconda]: https://docs.continuum.io/anaconda/install
[jupyter]: http://jupyter.org/
[markdown]: https://en.wikipedia.org/wiki/Markdown
[gapminder]: http://gapminder.org
