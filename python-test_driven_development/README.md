# Test-driven development
As we all know, if nobody ever tested their code, we'd have a hard time using any app or website at all. Which is why we're embarking on this great journey of learning how to test first and code second.
## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All files end with a new line
* All test files (.txt) should be inside a folder `tests`
* All tests should be executed with `python3 -m doctest ./tests/*`
* All modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
* The length of all files will be tested using wc
* Importing modules is strictly forbidden
## Tasks
### General information
__Number of tasks:__ 6<br/>
__Completed:__ TBA<br/>
__Passed:__ TBA<br/>
### Testing our drive, our patience, and more
It's all about being thorough while not forgetting to stop for a good meal.
#### 0. Integers addition
In `0-add_integer.py`, add integers `a` and `b` after converting them from float if need be.<br/>
If the arguments are not integers or floats, raise a `TypeError` exception.<br/>
In `/tests/0-add_integer.txt`, test for edge cases as well as the regular expected exceptions.
#### 1. Divide a matrix
In `2-matrix_divided.py`, divide all elements of a matrix by `div`.<br/>
If `div` is not an integer or a float > 0, raise the corresponding exception.<br/>
In `tests/2-matrix_divided.txt`, test for edge cases as well as the regular expected exceptions.
#### 2. Say my name
In `3-say_my_name.py`, print `My name is <first name> <last name>`.<br/>
If any argument isn't a string, raise a `TypeError` exception:<br/>
- first_name must be a string
- last_name must be a string
In `tests/3-say_my_name.txt`, test for edge cases as well as the regular expected exceptions.
#### 3. Print square
In `4-print_square.py`, print a square of size `size` using the character `#`.<br/>
If `size` isn't an integer or is < 0, raise the corresponding exception:<br/>
- size must be an integer
- size must be >= 0
In `tests/4-print_square.txt`, test for edge cases as well as the regular expected exceptions.
#### 4. Text indentation
In `5-text_indentation.py.py`, the characters: `.`, `?` and `:` will be followed by two new lines when we print `text`.<br/>
If `test` isn't a string, raise the `TypeError` exception message `"text must be a string"`.<br/>
In `tests/5-text_indentation.py.txt`, test for edge cases as well as the regular expected exceptions.
#### 5. Max integer - Unittest
In `tests/6-max_integer_test.py`, write unittests for the function `def max_integer(list=[]):`.
We are allowed to use the `unittest` module.