---
title: "Tuples & Dictionaries"
teaching: 10
exercises: 5
questions:
- "How can I add semantic value to my collections of multiple values?"
objectives:
- "Identify lists, tuples and dictionaries"
- "Write programs that create and modify dictionaries"
- "Select the best data collection type for a given purpose."
keypoints:
- "A tuple is a list that can never be changed."
- "Use an item's index to fetch it from a tuple."
- "Dictionaries are lists in which the semantic meaning of each entry is more important than its order."
- "New entries can be added to an existing dictionary by assignment."
- "Dictionary keys are unique - only one item can exist per key"
- "Use `del` to remove items from a list entirely"
- "You can access all the keys and all the values of a dictionary"
- "Collections (lists, tuples, dictionaries) may be nested arbitrarily"
- "Code clarity & maintainability should guide choice of collection type"
---
## Tuples are "immutable" lists

*   Sometimes it is useful to "bind" different pieces of data together.
*   Tuples can be indexed like lists

~~~
name = ('Paul', 'Wilson')
first_name = name[0]
last_name = name[1]
print(first_name,last_name)
~~~
{: .python}

*   Individual entries in tuples cannot be changed

~~~
name = ('Paul', 'Wilson')
name[1] = 'Nagus-Wilson'
~~~
{: .python}
~~~
TypeError                                 Traceback (most recent call last)
<ipython-input-85-8f02ace9e6af> in <module>()
      1 name = ('Paul','Wilson')
----> 2 name[1] = 'Nagus-Wilson'

TypeError: 'tuple' object does not support item assignment
~~~
{: .error}

## Immutability preserves order

*   Lists of tuples are better than parallel lists
*   Can't accidentally change data that is presumed to correspond

~~~
first_names = ['Paul', 'Patrick', 'Sarah']
last_names = ['Wilson', 'Shriwise', 'Stevens']
last_names[1] = 'Nagus-Wilson'
print(first_names)
print(last_names)
names = [('Paul','Wilson'), ('Patrick','Shriwise'), ('Sarah','Stevens')]
print(names[0])
~~~
{: .python}

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


## All collection types can be nested

*   Lists, tuples and dictionaries may all contain lists, tuples and dictionaries

~~~
instructors = [{'first':'Paul', 'middle': 'Philip', 'last':'Wilson'},       # list of dictionaries
               {'first':'Sarah','last':'Stevens'},
               {'first':'Patrick','last':'Shriwise'}]
axes_tics = {'x': [0,0.1,0.2,0.3,0.4,0.5],              # dictionary of lists
             'y': [0,10,20,30,40,50]}
curve_points = [(0,0), (2,3), (4,5), (6,-3), (8,-10)]   # list of tuples
shapes = { 'shape_01': [(0,0), (3,4), (6,-3), (10,-6)], # dictionary of lists of tuples
           'other_shape': [(12,4.5), (15,10), (4,78)] }
print(shapes)
~~~
{: .python}

*   Defining collections as above looks cumbersome.  Often collections are defined
    more programmatically, a little at a time, rather than in a single big block.

## Choosing the best data structure

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
