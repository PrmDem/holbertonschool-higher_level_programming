# Abstract Base Classes
Here we'll delve into a magical pond where ducks take classes about abstract yet substandard maths.<br/>
That doesn't look quite right...<br/>
## Tasks
### General information
__Number of tasks:__ 6<br/>
__Completed:__ 1<br/>
__Passed:__ TBA<br/>
### Overview
#### 0. Abstract Animal Class and its Subclasses
Creates abstract class Animal and its abstract method `sound`.<br/>
Then, adds subclasses Dog and Cat where `sound` will be implemented.<br/>
See file [`task_00_abc.py`](./task_00_abc.py).
#### 1. Shapes, Interfaces, and Duck Typing
The abstract class `Shape` takes two abstract methods, `area` and `perimeter`.<br/>
Two concrete classes, `Circle` and `Rectangle`, will inherit from `Shape` and implement these methods.<br/>
Lastly, a "standalone function" `shape_info` will print both of these attributes for any instance of a `Shape` subclass.<br/>
See file [`task_01_duck_typing.py`](./task_01_duck_typing.py).
#### 2. Extending the Python List with Notifications
The class `VerbpseList`, which inherits from class `list`, will have overrides for methods `append`, `extend`, `remove`, and `pop`.<br/>
See file [`task_02_verboselist.py`](./task_02_verboselist.py).
#### 3. CountedIterator - Keeping Track of Iteration
Overriding `__next__` from `iter` this time, adds a counter for the number of items iterated over.<br/>
See file [`task_03_countediterator.py`](./task_03_countediterator.py).
#### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Creating a class `FlyingFish` which inherits from both the `Fish` and `Bird` classes, overrides their methods and prints info in the right order (`MRO` exploration).<br/>
See file [`task_04_flyingfish.py`](./task_04_flyingfish.py).
#### 5. The Mystical Dragon - Mastering Mixins
Employs `mixins` to marvel at a dragon's abilities. As we should.<br/>
See file [`task_05_dragon.py`](./task_05_dragon.py).