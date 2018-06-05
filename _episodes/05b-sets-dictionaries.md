---
title: "Sets and Dictionaries"
teaching: 10
exercises: 5
questions:
- "What is a set?"
- "What is a dictionary?"
objectives:
- "Explain the features of sets and dictionaries."
- "Understand how dictionaries map keys to values"
- "Learn how to add and get items from sets and dictionaries."
keypoints:
- "A set is an unordered, unique collection of immutable objects."
- "A dictionary is a mapping between objects, from **keys** to **values**."
- "Dictionary keys must be immutable."
- "Get a value from a dictionary with `my_dict[some_key]`. Add an item with `my_dict[some_key] = some_value`."
- "Dictionaries and sets are mutable."
---

# Sets
## Sets are unordered collections of *unique* items
*    Construct a set with braces: `my_set = {object1, object2, object3, ...}`
     * You can also use the built-in `set()` function to make a set from another
       iterable: `my_set = set("abc")`
*    Sets in Python behave like mathematical sets
     * Support common set operations (as methods): 
     * `my_set.union()`, `my_set.difference()`, `my_set.intersect()`

~~~
set1 = set("abc")
set2 = set("acb")
set3 = set("aabbbcc")
print(set1, set2, set3)
~~~
{: .python}
~~~
{'b', 'c', 'a'} {'b', 'c', 'a'} {'b', 'c', 'a'}
~~~
{: .output}

*    Add items to a set using the `add()` and `update()` methods

~~~
my_set = {'a', 'b', 'c'}
my_set.add('d')
print(my_set)

my_set.update({'e', 'f', 'g'})
print(my_set)
~~~
{: .python}
~~~
{'a', 'c', 'd', 'b'}
{'f', 'g', 'b', 'e', 'c', 'd', 'a'}
~~~
{: .output}

*    Get an element from a set using `pop()`
*    This returns an element from the set **and removes it**

~~~
some_set = set(['UGA', 'UAG', 'UAA'])
print(some_set)
print(some_set.pop())
print(some_set)
~~~
{: .python}
~~~
{'UAG', 'UAA', 'UGA'}
UAG
{'UAA', 'UGA'}
~~~
{: .output}

> ## What objects can go in a set?
> Suprisingly, not type of object can be added to a set
> ~~~
> my_set = {[1, 2]}
> ~~~
> {: .python}
> ~~~
> ---------------------------------------------------------------------------
> TypeError                                 Traceback (most recent call last)
> <ipython-input-4-bf858b2308e0> in <module>()
> ----> 1 my_set = {[1, 2]}
>  
> TypeError: unhashable type: 'list'
> ~~~
> {: .error}
> - The error means that python cannot add a list to a set
> - Only objects that **cannot change** can be added to sets
{: .challenge}

# Dictionaries
## Dictionaries add meaningful labels

*    Once you start binding data together, it is often useful to add
     semantic meaning
*    Dictionaries allow you to label the entries that are bound together
     * Be sure to choose meaningful names!
*    Dictionaries are mutable, you can change them
     *   Because of meaningful labels, this is less dangerous
*    Dictionaries map **keys** to **values**: `my_dict = {key1:value1, key2:value2, ...}`
     * As with sets, **dictionary keys must be guaranteed not to change**

~~~
name = {'first': 'Paul', 'last': 'Wilson'}
print(name['first'], name['last'])
name['last'] = 'Nagus-Wilson'
print(name['first'], name['last'])
~~~
{: .python}
~~~
Paul Wilson
Paul Nagus-Wilson
~~~
{: .output}

## Entries can be added to a dictionary

*    As long as the variable is already of a dictionary type, new entries can be
     added as if they were already there
*    Only one item can exist for each unique key
     * Assigning a new value to an existing key overwrites the old value

~~~
my_name = {'first': 'Paul', 'last': 'Wilson'}
my_name['middle'] = 'Philip'
print(my_name)
my_name['last'] = 'Nagus-Wilson'
print(my_name)
your_name['first'] = 'Henry'
~~~
{: .python}
~~~
{'first': 'Paul', 'last': 'Wilson', 'middle': 'Philip'}
{'first': 'Paul', 'last': 'Nagus-Wilson', 'middle': 'Philip'}
~~~
{: .output}
~~~
--------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-97-cc04cabb3603> in <module>()
      1 my_name = {'first': 'Paul', 'last': 'Wilson'}
      2 my_name['middle'] = 'Philip'
----> 3 your_name['first'] = 'Henry'

NameError: name 'your_name' is not defined
~~~
{: .error}


## Use `del` to remove items from a dictionary entirely.

~~~
my_name = {'first': 'Paul', 'middle': 'Philip', 'last': 'Wilson'}
print(my_name)
del my_name['middle']
print(my_name)
~~~
{: .python}
~~~
{'first': 'Paul', 'middle': 'Philip', 'last': 'Wilson'}
{'first': 'Paul', 'last': 'Wilson'}
~~~
{: .output}

## Various ways to access all the entries in a dictionary

*   The names of each entry are called `keys`
*   The values of each entry are called `values`

~~~
name = {'first': 'Paul', 'last': 'Wilson'}
print(name.keys())
print(name.values())
~~~
{: .python}
~~~
dict_keys(['first', 'last'])
dict_values(['Paul', 'Wilson'])
~~~
{: .output}