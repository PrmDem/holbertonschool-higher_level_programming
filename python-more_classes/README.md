# MORE classes !!!
This project is our second approach to Python classes.<br/>These tasks also build on each other, just like in python-classes.
## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All files end with a new line
* The length of all files will be tested using wc
* We are not allowed to import any module
## Tasks
### General information
__Number of tasks:__ 10<br/>
__Completed:__ 9<br/>
__Passed:__ TBA<br/>
### Overview
We just learned to output a square, so now it's time to up the ante...<br/>
With _rectangles_ !
#### 0. Simple rectangle
Defines a rectangle through the class `Rectangle`.<br/>
See file [`0-rectangle.py`](./0-rectangle.py).
#### 1. Real definition of a rectangle
Adds private instance attributes `width`and `height`, with a getter and a setter for each.<br/>
Type and Value errors will be raised should the passed arguments not be integers or be under 0.<br/>
See file [`1-rectangle.py`](./1-rectangle.py).
#### 2. Area and Perimeter
Adds public instance methods `def area(self)`, which returns the rectangle area, and `def perimeter(self)`, which returns – you guessed it – the rectangle's perimeter.<br/>
See file [`2-rectangle.py`](./2-rectangle.py).
#### 3. String representation
Ensures using `print()` and `str()` outputs our rectangle, which is made up of `#`s.
See file [`3-rectangle.py`](./3-rectangle.py).
#### 4. Eval is magic
Using `repr()` then `eval()` allows us to create a brand new, separate rectangle.<br/>
See file [`4-rectangle.py`](./4-rectangle.py).
#### 5. Detect instance deletion
Prints the heartbreaking message `Bye rectangle...` whenever a rectangle is deleted. Goodbye, soldier.<br/>
See file [`5-rectangle.py`](./5-rectangle.py).
#### 6. How many instances
Adds a public class attrubute `number_of_instances`.<br/>
Initialised to 0, it is incremented upon instantiation and decremented upon deletion of an instance.<br/>
See file [`6-rectangle.py`](./6-rectangle.py).
#### 7. Change representation
Adds public class attribute `print_symbol`.<br/>
Initialised to `#`, it can be any type and will be used for string representation.<br/>
See file [`7-rectangle.py`](./7-rectangle.py).
#### 8. Compare rectangles
Implements static method `def bigger_or_equal(rect_1, rect_2):`, which returns biggest rectangle based on area.<br/>
Both parameters, `rect_1` and `rect_2`, must be an instance of `Rectangle` or a `TypeError` will be raised.<br/>
Should both rectangles have the same area value, `rect_1` will be returned.<br/>
See file [`8-rectangle.py`](./8-rectangle.py).
#### 9. A square is a rectangle
The new class method `def square(cls, size=0)` returns a new Rectangle instance where `width == height == size`.
See file [`9-rectangle.py`](./9-rectangle.py).