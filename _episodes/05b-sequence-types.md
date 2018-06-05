---
title: "Sequence Types: Strings, Tuples and Lists"
teaching: 20
exercises: 10
questions:
- "What is a Sequence in Python?"
- "What is the difference between strings, tuples, and lists?"
- "How can we access items in a Sequence?"
objectives:
- "Explain the features of strings, tuples, and lists."
- "Determine when to use strings, tuples, or lists to store data."
- "Access specific items in a Sequence by position."
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

# What is a Sequence?
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


> ## What can you do with strings?
> 
> Can you use the `+` and `*` operators on strings?
> 
> What do you expect the value of `full_name` to be?
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


# Accessing items in a Sequence

## Use an index to get a single object from a sequence.

- The objects in a sequence are ordered. For example, the string 'AB' is not the same as 'BA'.

-  Because of this ordering, we can give each item a number that is it's position in the sequence. This

  number is called an index or sometimes a subscript.

- Indices are numbered from 0.

- Use the position's index in square brackets to get the item at that
  position.

~~~
first_name = "Taylor"
print(first_name[0])

full_name = ("Taylor", "Dean", "Scott")
middle_name = full_name[1]
print(middle_name)

swc_instructors = ["Matt Garcia", "Kalin Kiesling", "Taylor Scott", "Patrick Shirwise"]
an_instructor = swc_instructors[2]
~~~
{: .python}
~~~
T
Dean
Taylor Scott
~~~
{: .output}


## Use a slice to get a substring.

- A part of a string is called a substring. A substring can be as short as a
  single character.
- An item in a list is called an element. Whenever we treat a string as if it
  were a list, the string's elements are its individual characters.
- A slice is a part of a string (or, more generally, any list-like thing).
- We take a slice by using `[start:stop]`, where `start` is replaced with the
  index of the first element we want and `stop` is replaced with the index of
  the element just after the last element we want.
- Mathematically, you might say that a slice selects `[start:stop)`.
- The difference between stop and start is the slice's length.
- Taking a slice does not change the contents of the original string. Instead,
  the slice is a copy of part of the original string.

~~~
print(first_name[0:2])
~~~

{: .python}

~~~
Ah
~~~
{: .output}

## Slicing

What does the following program print?

~~~
atom_name = 'carbon'
print('atom_name[1:3] is:', atom_name[1:3])
~~~
{: .python}
~~~
atom_name[1:3] is: ar
~~~
{: .output}

1. What does `thing[low:high]` do?
2. What does `thing[low:]` (without a value after the colon) do?
3. What does `thing[:high]` (without a value before the colon) do?
4. What does `thing[:]` (just a colon) do?
5. What does `thing[number:negative-number]` do?
   {: .challenge}

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
> If Python starts counting from zero,
> and `len` returns the number of characters in a string,
> what index expression will get the last character in the string `name`?
> (Note: we will see a simpler way to do this in a later episode.)
>
>> ## Solution
>> ~~~
>> name[len(name) - 1]
>> ~~~ 
>> {: .python}
>{: .solution}
{: .challenge}