---
title: "Other Data Types"
teaching: 5
exercises: 0
questions:
- "What are True, False, and None?"
objectives:
- "Learn why True, False, and None are different from other datatypes"
keypoints:
- "`True`, `False`, and `None` are special keywords in Python"
- "There is only ever one object called `True`, `False`, or `None`"
---

# True, False, and None are special data types

 - As their names suggest, use them to store information about whether
 data is true, false, or does not exist
 - Exactly one `True`, `False`, and `None` object everytime Python runs

~~~
a = None
b = None
print(id(a), id(b))
~~~
{: .python}
~~~
1563782080 1563782080
~~~
{: .output}