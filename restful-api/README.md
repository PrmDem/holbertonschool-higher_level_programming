# RESTful API
Learning API consumption, development, security & documentation.<br/>
## Requirements
* Allowed editors: vi, vim, emacs
* All files will be interpreted on Ubuntu 20.04 LTS using python3 (version 3.8.*)
* All files end with a new line, and start with `#!/usr/bin/python3`
* All files must be executable
* All files should use pycodestyle (version 2.7.*)
## Tasks
### General information
__Number of tasks:__ 6<br/>
__Completed:__ 6<br/>
__Passed:__ 6<br/>
### Overview
#### 0. Basics of HTTP/HTTPS
Take extended notes about the differences between HTTP and HTTPS.
#### 1. Consume data from an API using command line tools (curl)
Constructing and executing basic API requests with Curl — including setting headers, inspecting the output, and interpreting the results of common API requests.<br/>
#### 2. Consuming and processing data from an API using Python
Using the `requests` library to send HTTP requests and process responses, parsing and manipulating JSON data using Python, and converting structured data into other formats like CSV.<br/>
See file [`task_02_requests.py`](./task_02_requests.py).
#### 3. Develop a simple API using Python with the `http.server` module
With the `http.server`module, set up a basic API and implement several endpoints: `index`, `data`, `status`, `info`, and an `Endpoint not found` message on any other page.<br/>
See file [`task_03_http_server.py`](./task_03_http_server.py).
#### 4. Develop a Simple API using Python with Flask
Using `Flask` this time, define and handle routes to respond to different endpoints, serving JSON data. We will also handle POST requests to add new data to the API.<br/>
See file [`task_04_flask.py`](./task_04_flask.py).
#### 5. API Security and Authentication Techniques
Constructing various endpoints, this time differentiating between regular users and those with admin rights.<br>
See file [`task_05_basic_security`](./task_05_basic_security.py)