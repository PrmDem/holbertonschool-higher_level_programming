# Python : inheritance
Here we focus on the principle of _inheritance_ in Python.<br/>
Who thought classes couldn't get any cooler?<br/><br/>
## Requirements
### Script requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All files end with a new line, and start with `#!/usr/bin/python3`
* All files must be executable
* All files should use pycodestyle (version 2.7.*)
* We are not allowed to import any module
### Test cases requirements
* All test files should be inside a folder named `tests`
* All test files should be text files (extension: .txt)
* All tests should be executed by using the command `python3 -m doctest ./tests/*`
* All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
* All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
* All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
* The length of our documentation will be verified
* Using the i-word (which ends with 'mport') in our documentation may lead our checker to believe we're trying to do something forbidden, so it's best not to use that word in our docstrings at all. Same goes for 'from'.
## Tasks
### General information
__Number of tasks:__ 12<br/>
__Completed:__ 12<br/>
__Passed:__ 10<br/>
### Overview
#### 0. Lookup
Returns the list of available attributes and methods of an object.<br/>
See file [`0-lookup.py`](./0-lookup.py).
#### 1. My list
The class `MyList`, which inherits from `list`, has a method that prints the provided list in ascending order.<br/>
The list should only include elements of type `int`.<br/>
See file [`1-my_list.py`](./1-my_list.py) and [`1-my_list.txt`](tests/1-my_list.txt).
#### 2. Exact same object
Returns `True` if an object is an exact instance of a given class, `False` if not.<br/>
See file [`2-is_same_class.py`](./2-is_same_class.py).
#### 3. Same class or inherit from
Same as above, except we accept subclasses now.<br/>
See file [`3-is_kind_of_class.py`](./3-is_kind_of_class.py).
#### 4. Only sub class of
Same as above but not so much, as we're checking whether an object is an instance of a class that _inherits from_ a specific class.<br/>
See file [`4-inherits_from.py`](./4-inherits_from.py).
#### 5. Geometry module
Here we simply write an empty class named `BaseGeometry`.<br/>
See file [`5-base_geometry.py`](./5-base_geometry.py).
#### 6. Improve Geometry
Adds a public instance method to define area in the BaseGeometry class.<br/>
See file [`6-base_geometry.py`](./6-base_geometry.py).
#### 7. Integer validator
Adds the public instance method `integer_validator(self, name, value)`. It validates `value` as being an integer superior to 0.<br/>
See files [`7-base_geometry.py`](./7-base_geometry.py) and [`7-base_geometry.txt`](tests/7-base_geometry.txt).
#### 8. Rectangle
The class `Rectangle` inherits from `BaseGeometry`, and instantiates with `width`and `height`.<br/>
See file [`8-rectangle.py`](./8-rectangle.py).
#### 9. Full rectangle
Adds full implementation of `area` method. `[Rectangle] <width>/<height>` is returned by `str()` and printed by `print`.<br/>
See file [`9-rectangle.py`](./9-rectangle.py).
#### 10. Square #1
Adds the class `Square` which inherits from `Rectangle`. Instantiates with `size`.<br/>
See file [`10-square.py`](./10-square.py).
#### 11. Square #2
`[Square] <width>/<height>` is returned by `str()` and printed by `print`.<br/>
See file [`11-square.py`](./11-square.py).
