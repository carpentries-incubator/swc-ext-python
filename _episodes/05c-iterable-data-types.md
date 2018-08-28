---
title: "More on Iterable Data Types"
teaching: 5
exercises: 0
questions:
- "What do sequences, sets, and dictionaries have in common?"
- "How do they differ?"
- "When should I use each type?"
objectives:
- "Explain what it means for a data type to be iterable."
- "Understand the difference between ordered and unordered types."
- "Explain  how a mutable data type differs from an immutable data type."
- "Understand when to use one iterable type versus another."
keypoints:
- "Iterable data types are collections of objects."
- "Ordered data types perserve the order of creation."
- "Unordered data types return data in a random order."
- "Mutable data types can be changed in place."
- "Immutable data types cannot be changed in place. To modify them, you must create a new object."
- "All iterable types have a *length*, the number of items they hold"
- "Choose an iterable type that makes your code safer and easier to understand."
---

# What is an iterable data type?

### What is iteration?

* The types we just learned (strings, lists, tuples, sets, and dictionaries)
 are all collections of things.
* Iteration is going through a collection item-by-item

> ## Example
>
> * Translating a collection of DNA sequences into protein sequences
> * Get the atomic number of every element in a molecule
> * Calculate the mean of 3 measurements at every timepoint
{: .callout}

### What are the iterable data types?

* Collection types are often called **iterable**
* As we've seen, Python has 5 basic iterable data types
	* Strings
	* Tuples
	* Lists
	* Sets
	* Dictionaries
* These data types have different features and are used for different types of data
* It's helpful to consider whether these types are **ordered** or **unordered**
and whether they are **mutable** or **immutable**.


# Ordered vs. Unordered Types

Try running the following:

~~~
my_list = list('abc')
my_set = set('abc')

print('my_list = ', my_list)
print('my_set = ', my_set)
~~~
{: .python}

What do you notice about the result of printing `my_list` and `my_set`?

> ## Solution
>
> ~~~
> my_list = ['a', 'b', 'c']
> my_set = {'b', 'c', 'a'}
> ~~~
> {: .output}
{: .solution}

* **Ordered** types maintain the order in which they were created
* **Unordered** types do not maintain this order

> ## Challenge
>
> * Is unordered the same as random?
> * Will the same thing print each time?
>
> ~~~
> print(set('abc'))
> print(set('bca'))
> print(set('cba'))
> ~~~
> {: .python}
>
>> ## Solution
>> ~~~
>> {'b', 'c', 'a'}
>> {'b', 'c', 'a'}
>> {'b', 'c', 'a'}
>> ~~~
>> {: .output}
>>
>> Unordered means you can't *depend* on any particular order
>> * The order may change when you upgrade python
>> * It may also change the next time you run your program
> {: .solution}
{: .callout}

# Mutable vs Immutable Types

* Mutability is a tricky subject and the cause of *many* python bugs
* Some types can be modified "in place", that is the original object is changed
instead of creating a new object
* If an object can be modified in place it is **mutable**; otherwise it is **immutable**

> ## Example
>
> Run the following code. What's the difference?
>
> ~~~
> my_list = ['a', 'b', 'c']
> also_my_list = my_list
>
> my_string = 'abc'
> also_my_string = my_string
>
> my_list.extend(['d', 'e', 'f'])
> my_string = my_string + "def"
>
> print('my_list = ', my_list)
> print('also_my_list = ', also_my_list)
>
> print('my_string = ', my_string)
> print('also_my_string = ', also_my_string)
> ~~~
> {: .python}
>
>> ## Solution
>>  * Modifying `my_list` also modifies `also_my_list`
>>  * Modifying `my_string` does not change `also_my_string`
>>
>> ~~~
>> my_list =  ['a', 'b', 'c', 'd', 'e', 'f']
>> also_my_list =  ['a', 'b', 'c', 'd', 'e', 'f']
>> my_string =  abcdef
>> also_my_string =  abc
>> ~~~
>> {: .output}
> {: .solution}
{: .callout}

# Iterables have lengths

- The `len()` function gives the number of things in a collection

~~~
print(len("abc"))
print(len([1, 2, 3, 4]))
~~~
{: .python}
~~~
3
4
~~~
{: .output}

- Numbers do not have a length

```
print(len(52))
```
{: .python}

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-3-f769e8e8097d> in <module>()
----> 1 print(len(52))

TypeError: object of type 'int' has no len()
```
{: .error}


# Choosing the best data structure

*   **Best Practice: Write programs for people and not for computers!**
*   The best choice of data structure depends on how you will use it
*   Focus on clarity before performance
*   Good data structure choices can make your code easier to follow

### Lists & Tuples vs Dictionaries

*   Does the data have a natural order?
    *  Yes &rarr; consider a list, dictionaries can be sorted by their keys, but
       order is not inherent
    *  All access to list data is either by looping through it in order, or by
       referring to an entry by it's ordinal place in the list
    *  All access to dictionary data is either by looping through it, perhaps
       in some arbitrary order, or by referring to an entry by it's semantic meaning
*   Does the addition of keys add semantic value?
    *  Yes &rarr; probably benefit from a dictionary
    *  No  &rarr; fabricating keys that don't have semantic value can be counter-productive
        * If the order of entries **IS** the semantic value, then use a list

### Lists vs Tuples

*   Do you want to clearly indicate that certain data has an immutable relationship?
    * Yes &rarr; choose a tuple; immutability provides a weak form of semantics
      since order is fixed

### Comparison of Collection Data Structures

#### List

**Used When/For:** Simple Collection of Elements

* Has a consistent order
* Finding items may require inspecting all elements
* Elements indexed/accessed by numeric position

#### Set

**Used When/For:** *Unique* Collection of Elements

* Has a random order
* Finding elements will be fast

#### Tuple

**Used When/For:** *Immutable* Collection of Elements

* All elements in collection must be present at creation
* Immutability is useful to protect data from unintended changes

#### Dictionary

**Used When/For:** *Named* Collection of Elements

* Collections indexed by keys
* Can encode simple object-like data structures
* Has random order
* Lookup/retrieval by key will be fast
* Simple data structures behave like temporary in-memory databases
