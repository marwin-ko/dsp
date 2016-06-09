# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists and tuples are both iterables and type agnostic. On the other hand, Lists are mutable(change be changed) and tuples are immutable (cannot be changed). Tuples will work as keys in dictionaries since it is a hashable type. Lists cannot be used as keys since lists can be modified in place and is an unhashable type.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are both mutable, iterables, and type agnostic. However, lists are ordered and sets are unordered. In addition, sets only contain unique elements (i.e. there is only one of each element with resepect to both symbol and type). 
```
# Examples
st = {1,2,3,4,4,'4','a'}    # set
ls = ['1',2,3,'4',4,4,'a']  # list
```
In terms of performance with respect to time-complexity, Big O, the look up time (average case senario) for a list and set is O(n) and O(1), respectively. A list traverses through itself to search for an element which makes the search time dependent on the n number
of elements in the list, hence it's look up is O(n). On the other hand, since sets only contain unique elements they
use a hastable to lookup elements which is a O(1) lookup time.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is used in function programming, a style of programming based around functions.
The lambda function creates an anonymous function where that respective function
is not bound to a name. This helps reduce the quantity of code written, i.e. using lambda
instead of creating a function using def and return. Typically, the lambda function is
coupled with other functions such as filter(), reduce(), and map() to filter out elements,
reduce an interable into a single value, and applies function to each individual element of an iterable.
```
# Example
people = [(9,'Marwin','5''7"'),(3,'John','6''0"'),(5,'Draymond','6''5"'),(1,'Steph','6''3"')]
print sorted(people,key=lambda x:x[0])
# OUTPUT ==> [(1, 'Steph', '63"'), (3, 'John', '60"'), (5, 'Draymond', '65"'), (9, 'Marwin', '57"')]
```
---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

A list comprehension is a method that generates a list based on some logic or function. Specifically in a list comprehension, a loop is embedded into a [] that can be coupled with logical statements (e.g. if).
```
# Example (list comprehension)
odd_cubes_LC = [x**3 for x in range(11) if x**3%2==1]

# Example (map)
odd_cubes_MAP = []
for i in map(lambda x:x**3, range(11)):
    if i%2==1:
        odd_cubes_MAP.append(i)
        
# Example (filter)
cubes = []
for i in range(11):
    cube = i**3
    cubes.append(cube)
odd_cubes_FT = filter(lambda x: x%2==1, cubes)

# Example (map & filter)
cubes = map(lambda x:x**3, range(11))
odd_cubes_MF = filter(lambda x: x%2==1, cubes)
```
A list comprehension encompasses the lambda, map(), and filter() fuctions.
The first portion of a list comprehension iteratively manipulates some iterable
which is equivalent to the map() function used in conjunction with lambda. The
latter half of the list comprehension can incorporate an if statement which is
equivalent to the filter() function used in conjunction with lambda.
```
# Example (set comprehension)
set_comp = {x**3 for x in range(11) if x**3%2==1}

# Example (dictionary comprehension)
dict_comp = {i:i**3 for i in range(11) if i**3%2==1}
```
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 Days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 Days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 Days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





