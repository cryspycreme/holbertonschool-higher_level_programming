# Understanding Python Objects: A Beginner’s Guide

### Introduction

In Python, **everything is an object**. Whether it’s a number, string, list, or even a function, each variable you create is a reference to an object stored in memory. Objects have **identity**, **type**, and **value**, and understanding how Python handles them is key to writing correct and efficient code. For example:

```python
x = 42
y = "hello"
z = [1, 2, 3]
```

Here, `x`, `y`, and `z` all refer to different objects in memory with their respective types and values.

---

### id and type

Each object in Python has a unique identity, which you can check using `id()`, and a type, which you can check using `type()`. For example:

```python
a = 10
b = a
print(id(a), id(b))   # Same id since integers are immutable and small ints are reused
print(type(a), type(b))  # <class 'int'> <class 'int'>
```

Even though `a` and `b` have the same value and type, the `id()` function shows their unique memory location, which matters when determining if two variables refer to the same object.

---

### Mutable objects

**Mutable objects** can be changed in place after they are created. Lists, dictionaries, and sets are common examples. For instance:

```python
lst = [1, 2, 3]
alias = lst
lst.append(4)
print(lst)    # [1, 2, 3, 4]
print(alias)  # [1, 2, 3, 4] – both names refer to the same object
```

Here, `lst` and `alias` are **aliases** of the same list object. Changing one affects the other because lists are mutable and Python does not create a copy when assigning one variable to another.

---

### Immutable objects

**Immutable objects** cannot be changed once they are created. Numbers, strings, and tuples are common examples. For example:

```python
s = "hello"
t = s
s = s + " world"
print(s)  # "hello world"
print(t)  # "hello" – original object is unchanged
```

The `+` operation on strings creates a **new object**, leaving the original string unchanged. This shows how immutability ensures that the original object remains safe from accidental modifications.

---

### Why it matters: how Python treats mutable vs immutable objects

The distinction between mutable and immutable objects affects how Python handles assignment, operations, and memory. For mutable objects, assigning one variable to another creates an alias, meaning changes to one variable are reflected in the other. For immutable objects, Python often reuses objects for efficiency and creates new objects when “modifications” occur:

```python
a = [1, 2, 3]
b = a
a += [4]          # mutates the list
print(b)          # [1, 2, 3, 4]

x = 100
y = x
x += 50           # creates a new int object
print(y)          # 100
```

Here, `+=` behaves differently for mutable vs immutable objects: the list was mutated in place, while the integer resulted in a new object.

---

### How arguments are passed to functions

Python passes **arguments by object reference**, meaning the function gets a reference to the same object. Whether the original variable changes depends on the object’s mutability. For example:

```python
def modify_list(lst):
    lst.append(99)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 99] – mutable object modified

def reassign_int(n):
    n = 50

x = 10
reassign_int(x)
print(x)        # 10 – immutable object unchanged
```

This demonstrates that **mutable objects can be changed inside functions**, while **immutable objects remain safe** because reassignment inside the function creates a new object locally.
