---
title: "Iterable Data Types"
teaching: 5
exercises: 0
questions:
- "What is iteration?"
- "What is the difference between ordered and unordered types?"
- "What is the difference between mutable and immutable types?"
objectives:
- "Explain what it means for a data type to be iterable."
- "Explain what ordered means in the context of iterable variables."
- "Explain  how a mutable data type differs from an immutable data type."
- "Explain the use of code blocks in episodes."
keypoints:
- "Iterable data types are collections of objects."
- "Ordered data types perserve the order of creation."
- "Unordered data types return data in a random order."
- "Mutable data types can be changed in place."
- "Immutable data types cannot be changed in place. To modify them, you must create a new object."
---

# What is an iterable data type?

### What is iteration?

* When programming you'll often be working with collections of things
* Iteration is going through a collection item-by-item

> ## Example
>
> * Translating a collection of DNA sequences into protein sequences
> * Get the atomic number of every element in a molecule
> * Calculate the mean of 3 measurements at every timepoint
{: .callout}
 
### What are the iterable data types?

* Python has 5 basic iterable data types
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
> my_list = list("abc")
> also_my_list = my_list
>
> my_tuple = tuple("abc")
> also_my_tuple = my_tuple
>
> my_list += list("def")
> my_tuple += tuple("def")
> 
> print('my_list = ', my_list)
> print('also_my_list = ', also_my_list)
> 
> print('my_tuple = ', my_tuple)
> print('also_my_tuple = ', also_my_tuple)
> ~~~
> {: .python}
> 
>> ## Solution
>>  * Modifying `my_list` also modifies `also_my_list`
>>  * Modifying `my_tuple` does not change `also_my_tuple`
>>
>> ~~~
>> my_list =  ['a', 'b', 'c', 'd', 'e', 'f']
>> also_my_list =  ['a', 'b', 'c', 'd', 'e', 'f']
>> my_tuple =  ('a', 'b', 'c', 'd', 'e', 'f')
>> also_my_tuple =  ('a', 'b', 'c')
>> ~~~
>> {: .output}
> {: .solution}
{: .callout}

# Iterables have lists

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