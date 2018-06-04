## You can use the "+" and "*" operators on strings.

- "Adding" character strings concatenates them.

```
full_name = 'Ahmed' + ' ' + 'Walsh'
print(full_name)
```

{: .python}

```
Ahmed Walsh
```

{: .output}

- Multiplying a character string by an integer _N_ creates a new string that consists of that character string repeated  _N_ times.
  - Since multiplication is repeated addition.

```
separator = '=' * 10
print(separator)
```

{: .python}

```
==========
```

{: .output}

## Strings have a length (but numbers don't).

- The built-in function `len` counts the number of characters in a string.

```
print(len(full_name))
```

{: .python}

```
11
```

{: .output}

- But numbers don't have a length (not even zero).

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