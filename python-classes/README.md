# Classes
In this project we'll make a first approach to Python classes.<br/>Every task builds on the one preceding it.
## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All files end with a new line
* All test files (.txt) should be inside a folder `tests`
* All tests should be executed with `python3 -m doctest ./tests/*`
* Each module, class, and method must contain docstring as comments.
* The length of all files will be tested using wc
* We are not allowed to import any module
## Tasks
### General information
__Number of tasks:__ 7<br/>
__Completed:__ 7<br/>
__Passed:__ TBA<br/>
### Overview
#### 0. My first square
Writes an empty class `square`that defines a square.<br/>
See file [`0-square.py`](./0-square.py).
#### 1. Square with size
Defines a square through instantiation of the private instance attribute `size`.<br/>
See file [`1-square.py`](./1-square.py).
#### 2. Size validation
Raises errors if `size` isn't an integer or is smaller than zero.<br/>
See file [`2-square.py`](./2-square.py).
#### 3. Area of a square
Adds public instance method `def area(self)` that returns the current square area.<br/>
See file [`3-square.py`](./3-square.py).
#### 4. Access and update private attribute
Now uses property and setter to access and update the value of `size`.<br/>
See file [`4-square.py`](./4-square.py).
#### 5. Printing a square
Adds public instance method `my_print(self)` to print a square to stdout, using the character `#`.<br/>
See file [`5-square.py`](./5-square.py).
#### 6. Coordinates of a square
Adds `position` to instantiation of a square.<br/>
A number of blank spaces will be added at `position` in the printed square.<br/>
See file [`6-square.py`](./6-square.py).