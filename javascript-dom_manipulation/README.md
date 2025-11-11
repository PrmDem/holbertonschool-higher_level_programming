# JavaScript - DOM Manipulation
In this project, we learn how to select HTML elements, modify the DOM (_Document Object Model_), make requests, and use the event listener.<br/>
We will be reviewed by our peers, ensuring we all have a good enough understanding of the subject matter.<br/>

## Requirements
* All editors are allowed
* All files will be interpreted on Chrome browser (version 57.0 or later)
* All files should end with a new line
* A README with meaningful information about the content is mandatory
* Code should be semistandard compliant
* `var` cannot be used
* HTML should not reload for each action: DOM manipulation, update values, fetch data…

## General information
__Number of tasks:__ 9<br/>
__Completed:__ 9<br/>
__Passed:__ TBA<br/>

## Overview
#### 0. Color Me
Using `document.querySelector`, updates the text color of the header element to red (`#FF0000`).<br/>
See file [`0-script.js`](./0-script.js)
#### 1. Click and turn red
This time, the header element's text (id `red_header`) must turn red on click.<br/>
See file [`1-script.js`](./1-script.js)
#### 2. Add `.red` class
Adds the class `red` to the header element when the user clicks on the tag with id `red_header`.<br/>
See file [`2-script.js`](./2-script.js)
#### 3. Toggle classes
Toggles the class of the header element when the user clicks on the tag id `toggle_header`.<br/>
The header must have either the class 'red' or 'green', never none or both.<br/> 
See file [`3-script.js`](./3-script.js)
#### 4. List of elements
Adds a `li` element "_Item_" to a list when the user clicks on the element with id `add_item`.<br/>
See file [`4-script.js`](./4-script.js)
#### 5. Change the text
Updates the text of the header element to "_New Header!!!_" when the user clicks on the element with id `update_header`.<br/>
See file [`5-script.js`](./5-script.js)
#### 6. Star wars character
From <[this URL](https://swapi-api.hbtn.io/api/people/5/?format=json)> and using `Fetch API`, fetches a character's name and displays it in the html tag with id `character`.<br/>
See file [`6-script.js`](./6-script.js)
#### 7. Star Wars movies
Similarly to the prior task, retrieves all movie titles from <[this URL](https://swapi-api.hbtn.io/api/films/?format=json)> and lists them in the unordered list `list_movies`.<br/>
See file [`7-script.js`](./7-script.js)
#### 8. Say Hello!
From <[this URL](https://hellosalut.stefanbohacek.com/?lang=fr)>, fetches and displays the value of element 'hello' in the corresponding html tag.<br/> This must still work if imported from the head of our html file.
See file [`8-script.js`](./8-script.js)
