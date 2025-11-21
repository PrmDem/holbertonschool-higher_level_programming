# Everything is object
To deepen our understanding of Python and the 'object' type, this project will mostly ask us to answer questions based on snippets of code.<br/>
While `42` would be an acceptable answer every time, I will endeavor to bring a higher level of precision to my answers.<br/>

## Requirements
### Python scripts
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on _Ubuntu 20.04 LTS_ using `python3` (version 3.8.5)
* All files should start with `#!/usr/bin/python3` and end with a new line
* Code should use the pycodestyle (version 2.7.*)
* All files must be executable
* The length of the files will be tested using `wc`
### .txt answer files
* Should only be one line long
* No Shebang on the first line (i.e. “#!/usr/bin/python3”)
* All files should end with a new line

## General information
__Number of tasks:__ 30<br/>
__Completed:__ 29<br/>
__Passed:__ TBA<br/>

### Overview
#### Tasks 0 & 1
How do we get a variable's type or identifier ? Those burning questions finally have an answer.<br/>
See [task 0](./0-answer.txt), [task 1](./1-answer.txt).

#### Tasks 2 to 15
These focus on whether two variables are equal or truly the same. Hint: it depends on their type.<br/>
I won't link all of them here, for obvious reasons. Feel free to check out [task 2](./2-answer.txt) and continue from there.

#### Tasks 16 to 19, + 27 and 28
What happens to a variable that gets modified inside of a function, but does not get returned?<br/>
Where a list will be changed by an `append` method outside the scope of the function, another type of value assignment (incrementing an integer, assigning the value of list b to list a after an initial declaration) will not change the initial value of our variable without an explicit return.<br/>

#### Tasks 20 to 26
Tuples are immutable, which is a main difference between them and lists. These tasks take us through a similar path that the ones about lists, thus helping us figure out how exactly they differ.<br/>
