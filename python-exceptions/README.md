# Exceptions
```
A little less conversation, a little more exceptions please.
— Elvis
```
## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All files end with a new line
* The first line of all files is exactly #!/usr/bin/python3
* Code uses pycodestyle version 2.7.*
* All files are executable
* The length of all files will be tested using wc
## Tasks
### General information
__Number of tasks:__ 7<br/>
__Completed:__ TBA<br/>
__Passed:__ TBA<br/>
### What to except when you're excepting
#### 0. Safe list printing
Prints a certain number of elements from a list.<br/>That list can contain any types and we can be asked to print more than its length.<br/>We obviously have to use try/except, and we can't use `len()`, otherwise where's the fun?<br/>
See file `0-safe_print_list.py` if you like a party.
#### 1. Safe printing of an integers list
Prints an integer with `"{:d}".format()`.<br/>
We might not be given an integer though, and of course, we can't use `type()`.<br/>
See file `1-safe_print_integer.py` if that's your _type_ of exercise.
#### 2. Print and count integers
Prints the first x elements of a list, but only if they're integers.<br/>
Any other type of value must be 'skipped (in silence)' (sic).<br/>
See file `2-safe_print_list_integers.py` if you're in need of some peace and quiet.
#### 3. Integers division with debug
Divides two integers and prints the result.<br/>
We can finally use `finally` on top of `try` and `except`!<br/>
See file `3-safe_print_division.py` if you're happy about that.
#### 4. Divide a list
Divides two lists, element by element. Unless, of course, we can't...<br/>
See file `4-list_division.py` if that suspense really got you.
#### 5. Raise exception
Raises a type exception. That's all.<br/>
See file `5-raise_exception.py` if it feels a little abrupt.
#### 6. Raise a message
Raises a name exception – with a message.<br/>
See file `6-raise_exception_msg.py` if you want to know what the message is.