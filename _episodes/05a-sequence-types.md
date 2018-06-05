---
title: "Sequence Types: Strings, Tuples and Lists"
teaching: 20
exercises: 10
questions:
- "What is a sequence in Python?"
- "What is the difference between strings, tuples, and lists?"
- "How can we access items in a sequence?"
objectives:
- "Explain the features of strings, tuples, and lists."
- "Determine when to use strings, tuples, or lists to store data."
- "Access specific items in a sequence by position."
keypoints:
- "Strings, tuples, and lists are ordered collections of objects."
- "Strings and tuples are immutable."
- "Lists are mutable."
- "Strings are sequences of characters."
- "Tuples and lists can be of arbitrary (mixed) data types."
- "Unordered data types return data in a random order."
- "Access a specific item by its index with `sequence[index]`."
- "Access a range of items using slices: `sequence[start:stop:skip]`."
---

# What is a sequence?
- A sequence is an *ordered* collection of objects
- We've seen one example of a sequence already: strings are ordered collections of characters
- As we'll see, python also allows for sequences of arbitrary types

# Strings
- A string is an *ordered*, *immutable* sequence of characters
- Strings are constructed with quotes
  - Strings can be constructed with single quotes, double quotes, or triple quotes
    ~~~
    my_string = 'a sequence of characters'
    my_string = "a sequence of characters"
    my_string = '''a sequence of characters'''
    ~~~
    {: .python}
- Triple quoted strings can span multiple lines
  ~~~
  single_quote_string = 'a string on one line'
  triple_quote_string = '''a string
  on two lines'''
  ~~~
  {: .python}
- Strings can also be constructed with the `str()` function
  ~~~
  string_from_int = str(25)
  print(string_from_int)
  ~~~
  {: .python}
  ~~~
  '25'
  ~~~
  {: .output}


> ## Can you `+` and `*` strings?
> 
> What do you expect the value of `full_name` to be here?
> ~~~
> first_name = 'John'
> last_name = 'Smith'
> 
> full_name = first_name + ' ' + last_name
> ~~~
> {: .python}
>> ## Solution
>> ~~~
>> 'John Smith'
>> ~~~
>> {: .output}
>> - Adding two strings joins them together
>> - This is called **concatenation**
> {: .solution}
>
> What does `'3' * 10` produce? Is it what you expect? What about `'3' * '10'`?
>
>> ## Solution
>> - `'3' * 10 = '3333333333'`
>> - `'3' * '10'` gives a TypeError
>> - Multiplying a string an integer _N_ concatenates _N_ copies of the string
>> - Multiplying a string by a string is not allowed
> {: .solution}
{: .discussion}


# Lists

## A list stores many values in a single structure.

*   Doing calculations with a hundred variables called `pressure_001`, `pressure_002`, etc.,
    would be at least as slow as doing them by hand.
*   Use a *list* to store many values together.
    *   Contained within square brackets `[...]`.
    *   Values separated by commas `,`.

~~~
teen_primes = [12, 13, 17, 23]
~~~
{: .python}

## Appending items to a list lengthens it.

*   Use `list_name.append()` to add items to the end of a list.

~~~
primes = [2, 3, 5]
print('primes is initially:', primes)
primes.append(7)
primes.append(9)
print('primes has become:', primes)
~~~
{: .python}
~~~
primes is initially: [2, 3, 5]
primes has become: [2, 3, 5, 7, 9]
~~~
{: .output}

*   `append` is a *method* of lists.
    *   Like a function, but tied to a particular object.
*   Use `object_name.method_name` to call methods.
    *   Deliberately resembles the way we refer to things in a library.
*   We will meet other methods of lists as we go along.
    *   Use `help(list)` for a preview.
*   `extend` is similar to `append`, but it allows you to combine two lists.  For example:

~~~
teen_primes = [11, 13, 17, 19]
middle_aged_primes = [37, 41, 43, 47]
print('primes is currently:', primes)
primes.extend(teen_primes)
print('primes has now become:', primes)
primes.append(middle_aged_primes)
print('primes has finally become:', primes)
~~~
{: .python}
~~~
primes is currently: [2, 3, 5, 7, 9]
primes has now become: [2, 3, 5, 7, 9, 11, 13, 17, 19]
primes has finally become: [2, 3, 5, 7, 9, 11, 13, 17, 19, [37, 41, 43, 47]]
~~~
{: .output}

Note that while `extend` maintains the "flat" structure of the list, appending a list to a list makes the result two-dimensional.

## The empty list contains no values.

*   Use `[]` on its own to represent a list that doesn't contain any values.
    *   "The zero of lists."
*   Helpful as a starting point for collecting values
    (which we will see in a [later episode]({{page.root}}/06-for-loops/)).

## Lists may contain values of different types.

*   A single list may contain numbers, strings, and anything else.

~~~
goals = [1, 'Create lists.', 2, 'Extract items from lists.', 3, 'Modify lists.']
~~~
{: .python}

> ## From Strings to Lists and Back
>
> Given this:
>
> ~~~
> print('string to list:', list('tin'))
> print('list to string:', ''.join(['g', 'o', 'l', 'd']))
> ~~~
> {: .python}
> ~~~
> ['t', 'i', 'n']
> 'gold'
> ~~~
> {: .output}
>
> 1.  Explain in simple terms what `list('some string')` does.
> 2.  What does `'-'.join(['x', 'y'])` generate?
{: .challenge}


# Tuples

## Tuples are "immutable" lists
 - Like lists, can contain mixed data types
 - Defined with parenthesis and commas `my_tuple = (object 1, object 2, ...)`
 - Can be used to "bind together" two objects

 ~~~
 first_name = "John"
 last_name = "Smith"
 full_name = (first_name, last_name)
 print(full_name)
 ~~~
 {: .python}
 ~~~
 ('John', 'Smith')
 ~~~
 {: .output}


# Accessing items in a sequence

## Use an index to get a single object from a sequence.
 - The objects in a sequence are ordered. For example, the string 'AB' is not the same as 'BA'.
 -  Because of this ordering, we can give each item a number that is it's position in the sequence. This number is called an index or sometimes a subscript.
 - Indices are numbered from 0.
 - Use the position's index in square brackets to get the item at that position.

~~~
first_name = "John"
print(first_name[0])

full_name = ("John", "A", "Doe")
middle_initial = full_name[1]
print(middle_initial)

swc_instructors = ["Matt Garcia", "Kalin Kiesling", "Taylor Scott", "Patrick Shirwise"]
an_instructor = swc_instructors[2]
print(an_instructor)
~~~
{: .python}
~~~
J
A.
Taylor Scott
~~~
{: .output}

## Negative indices count backwards

*    The end of the sequence is indexed starting at `-1`
*    Negative indices can be used to get a sequence element

~~~
print(first_name[-1])
~~~
{: .python}
~~~
n
~~~
{: .output}

## Use the index to change an element of a list
 - Lists are mutable, so they can be changed in place
 - Use the index to replace an element of a list with a new value

~~~
small_primes = [2, 3, 5, 8, 9, 11]
print(small_primes)

small_primes[3] = 7
print(small_primes)
~~~
{: .python}
~~~
[2, 3, 5, 8, 9, 11]
[2, 3, 5, 7, 9, 11]
~~~
{: .output}

## Use `del` operator to remove an element from a list
 - `del` is a statement, not a function (so there are no parentheses)

~~~
print(small_primes)
del small_primes[4]
print(small_primes)
~~~
{: .python}
~~~
[2, 3, 5, 7, 9, 11]
[2, 3, 5, 7, 11]
~~~
{: .output}

## Strings and tuples are immutable.

*   Cannot change the characters in a string after it has been created.
*   Cannot change the elements of a tuple after it has been created.
    *   *Immutable*: can't be changed after creation.
    *   In contrast, lists are *mutable*: they can be modified in place.

~~~
element = 'carbon'
element[0] = 'C'
~~~
{: .python}
~~~
TypeError: 'str' object does not support item assignment
~~~
{: .error}


## Use a slice to get part of a selection.
- A slice is a part of a sequence.
- We take a slice by using `[start:stop]`, where `start` is replaced with the
  index of the first element we want and `stop` is replaced with the index of
  the element just after the last element we want.
- Mathematically, you might say that a slice selects `[start:stop)`.
- The difference between stop and start is the slice's length.
- Taking a slice does not change the contents of the original sequence. Instead,
  the slice is a copy of part of the original sequence.

~~~
print(first_name[0:2])
~~~

{: .python}

~~~
Jo
~~~
{: .output}

> ## Exercise
>  What does the following program print?
>
>  ~~~
>  atom_name = 'carbon'
>  print('atom_name[1:3] is:', atom_name[1:3])
>  ~~~
>  {: .python}
>  ~~~
>  atom_name[1:3] is: ar
>  ~~~
>  {: .output}
>
> 1. What does `thing[low:high]` do?
> 2. What does `thing[low:]` (without a value after the colon) do?
> 3. What does `thing[:high]` (without a value before the colon) do?
> 4. What does `thing[:]` (just a colon) do?
> 5. What does `thing[number:negative-number]` do?
   {: .challenge}
{: .discussion}

> ## Challenge
>
> If you assign `a = 123`,
> what happens if you try to get the second digit of `a`?
>
>> ## Solution
>>
>> Numbers are not stored in the written representation,
>> so they can't be treated like strings.
>>
>> ~~~
>> a = 123
>> print(a[1])
> ~~~
>> {: .python}
>> ~~~
> TypeError: 'int' object is not subscriptable
>> ~~~
>> {: .error}
> {: .solution}
{: .challenge}

## Last Character of a String
> ## Challenge
> We've seen one way to get the last character of a string.
> If Python starts counting from zero,
> and `len` returns the number of characters in a string,
> what is another index expression that will get the last character
> in the string `name`?
> Why might you prefer one over the other?
>
>> ## Solution
>> ~~~
>> name[len(name) - 1]
>> ~~~ 
>> {: .python}
>{: .solution}
{: .challenge}