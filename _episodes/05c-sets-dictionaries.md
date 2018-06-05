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
- "A set is an unordered, unique collection of **immutable** objects."
- "A dictionary is a mapping between objects, from **keys** to **values**."
- "Dictionary keys must be **immutable**."
- "Get a value from a dictionary with `my_dict[some_key]`. Add an item with `my_dict[some_key] = some_value`."
- "Dictionaries and sets are mutable."
---

# Sets


# Dictionaries
## Dictionaries add meaningful labels

*    Once you start binding data together, it is often useful to add
     semantic meaning
*    Dictionaries allow you to label the entries that are bound together
     * Be sure to choose meaningful names!
*    Dictionaries are mutable, you can change them
     *   Because of meaningful labels, this is less dangerous

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