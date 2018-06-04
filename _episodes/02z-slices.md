## Use an index to get a single character from a string.

- The characters (individual letters, numbers, and so on) in a string are
  ordered. For example, the string 'AB' is not the same as 'BA'. Because of
  this ordering, we can treat the string as a list of characters.
- Each position in the string (first, second, etc.) is given a number. This
  number is called an index or sometimes a subscript.
- Indices are numbered from 0.
- Use the position's index in square brackets to get the character at that
  position.

```
print(first_name[0])
```

{: .python}

```
A
```

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

```
print(first_name[0:2])
```

{: .python}

```
Ah
```

{: .output}

## Slicing

What does the following program print?

```
atom_name = 'carbon'
print('atom_name[1:3] is:', atom_name[1:3])
```

{: .python}

```
atom_name[1:3] is: ar
```

{: .output}

1. What does `thing[low:high]` do?
2. What does `thing[low:]` (without a value after the colon) do?
3. What does `thing[:high]` (without a value before the colon) do?
4. What does `thing[:]` (just a colon) do?
5. What does `thing[number:negative-number]` do?
   {: .challenge}

## Challenge

If you assign `a = 123`,
what happens if you try to get the second digit of `a`?

> ## Solution
>
> Numbers are not stored in the written representation,
> so they can't be treated like strings.
>
> ```
> a = 123
> print(a[1])
> ```
>
> {: .python}
>
> ```
> TypeError: 'int' object is not subscriptable
> ```
>
> {: .error}
> {: .solution}
> {: .challenge}

## Last Character of a String

If Python starts counting from zero,
and `len` returns the number of characters in a string,
what index expression will get the last character in the string `name`?
(Note: we will see a simpler way to do this in a later episode.)

> ## Solution
>
> `name[len(name) - 1]`
> {: .solution}
> {: .challenge}