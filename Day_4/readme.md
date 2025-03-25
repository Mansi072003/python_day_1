# Python Sequence Assignment

## 1. Define a sequence. What types of sequences exist in Python?
A sequence is an ordered collection of elements that supports indexing and slicing. Python has several sequence types, including:

- **Strings (`str`)**: Strings are immutable data type,therefore once deplayed,we can't alter the strings. 
- **Lists (`list`)**: A mutable sequence of elements.
- **Tuples (`tuple`)**: An immutable sequence of elements.
- **Ranges (`range`)**: A sequence representing an arithmetic progression.

## 2. How are strings, lists, and tuples different from each other?
- **Strings (`str`)**: Immutable and store characters.
- **Lists (`list`)**: Mutable and can store elements of different types.
- **Tuples (`tuple`)**: Immutable but can store elements of different types.

## 3. Explain how indexing works in Python with an example.
Indexing allows accessing elements of a sequence using their position. Python follows zero-based indexing, meaning the first element is at index `0`, the second at `1`, and so on. Negative indexing allows accessing elements from the end.

Example:
```python
text = "Python"
print(text[0])  # Output: P
print(text[-1]) # Output: n
```

## 4. How can we access the last character of a string?
Using negative indexing:
```python
text = "Python"
print(text[-1])  # Output: n
```

## 5. How do we create a list of numbers and access a specific element?
Lists are created using square brackets `[]`, and elements can be accessed using indexing.
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[2])  # Output: 30
```

## 6. What is the result of `len([1, [2, 3], 4])` and why?
The output is `3` because the list contains three elements: `1`, `[2, 3]`, and `4`. The inner list `[2,3]` is treated as a single element.

## 7. What is slicing in Python? Provide an example.
Slicing is used to extract a portion of a sequence. It uses the syntax `[start:stop:step]`, where:
- `start` is the index where slicing begins.
- `stop` is the index where slicing ends (exclusive).
- `step` defines the interval between elements.

Example:
```python
text = "Python Programming"
print(text[0:6])  # Output: Python
```

## 8. How do you reverse a string using slicing?
Using `[::-1]` to reverse the sequence:
```python
text = "Python"
print(text[::-1])  # Output: nohtyP
```

## 9. How does list concatenation and repetition work?
- **Concatenation (`+`)** combines two lists.
- **Repetition (`*`)** repeats a list multiple times.

Example:
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)  # Output: [1, 2, 3, 4, 5, 6]
print(list1 * 2)      # Output: [1, 2, 3, 1, 2, 3]
```

## 10. How can we count the occurrences of an element in a list?
Using the `count()` method:
```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # Output: 3
```

## 11. What will `print(my_tuple[1:])` output?
It will return a new tuple containing elements from index `1` to the end.
```python
my_tuple = (1, 2, 3)
print(my_tuple[1:])  # Output: (2, 3)
```

## 12. Difference between `list.append()` and `list.extend()`?
- **`append()`**: Adds an element as a single item.
- **`extend()`**: Adds elements from another iterable.

Example:
```python
lst = [1, 2]
lst.append([3, 4])  # Output: [1, 2, [3, 4]]
lst.extend([3, 4])  # Output: [1, 2, 3, 4]
```

## 13. How do we split a sentence into words?
Using `split()`:
```python
sentence = "Learn Python, step by step!"
print(sentence.split())
```

## 14. How do we join a list into a string?
Using `join()`:
```python
words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: "Python is fun"
```

## 15. How can we find the index of the first occurrence of an element?
Using `index()`:
```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.index(2))  # Output: 1
```

## 16. How do we check if a string is a palindrome?
```python
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  # Output: True
```

## 17. How do we find the length of the longest word in a sentence?
```python
def longest_word_length(sentence):
    return max(len(word) for word in sentence.split())

print(longest_word_length("Learn Python programming"))  # Output: 11
```

## 18. How does nested list indexing work?
```python
nested_list = [[1, 2], [3, 4, 5]]
print(nested_list[1][2])  # Output: 5
```

## 19. How do we convert a list of characters into a string?
Using `join()`:
```python
chars = ['P', 'y', 't', 'h', 'o', 'n']
print("".join(chars))  # Output: "Python"
```

## 20. How do we remove duplicates while preserving order?
Using a set:
```python
lst =[2,3,5,4,1,2,4,3,5,6]
res =[]
for i in lst:
    if i not in res:
        res.append(i)
print(sorted(res))  # Output: [1, 2, 3, 4]
```

## Sort a List of Tuples by the Second Element
```python
lst = [(1,4), (3,2), (5,6)]
res = []
for tup in lst:
    res.append(tup[1])
print(sorted(res))
```

## Flatten a Nested List of Arbitrary Depth
```python
lst = [[1,2,3], [4,5,6], [7,8,9]]  # Flattened output: [1,2,3,4,5,6,7,8,9]
res = []
for i in lst:
    for j in i:
        res.append(j)
print(res)
```

## Using Recursion
```python
def flatten(lst): 
    res = []
    for i in lst:
        if isinstance(i, list):  # Check if i is a list
            res.extend(flatten(i))  # Recursive call
        else:
            res.append(i)
    return res
print(flatten([[1,2,3], [4,5,6], [7,8,9]]))
```

# Rotate a List to the Right by k Steps
```python
def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    for i in range(k):
        last = lst[-1]
        for j in range(n-1, 0, -1):
            lst[j] = lst[j-1]
        lst[0] = last
    return lst
print(rotate_list([1,2,3,4,5], 2))    
```    

# Check if Two Strings are Anagrams
```python
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(anagram("listen", "silent")) 
```

# Split a List into Chunks of a Specified Size
```python
lst = [1,2,3,4,5,6,7,8,9]
n = 3
chunks = [lst[i:i+n] for i in range(0, len(lst), n)]
print(chunks)
```

# Merge Two Sorted Lists into One Sorted List
```python
def merge(l1, l2):
    l1.extend(l2)
    return sorted(l1)
print(merge([1,2,3], [4,5,6]))
```

