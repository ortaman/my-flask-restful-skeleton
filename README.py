Test
===========

### Requirements
python 3.6
pip3
virtualenv or vitualenwrapper

### Set up development environment
* Create and switch in your python enviroment.
* Install dependencies:
```sh
$ cd folder/to/clone-into/
$ pip3 install -r requirements.txt
```

* In the api directory run this project locally from the command line:
```sh
$  python app.py
```
* The application is running on :
```sh
http://localhost:5050/
```

### Tests

*  In the api directory run:
```sh
python -m pytest
```


### Exercise from a CLI
* Get the tool: `pip install httpie` and we can do the next requests:
```sh
http GET http://localhost:5050/api/v1/todos/todo1
http PUT http://localhost:5050/api/v1/todos/todo2 task=updated
http DELETE http://localhost:5050/api/v1/todos/todo3

http GET http://localhost:5050/api/v1/todos
http POST http://localhost:5050/api/v1/todos task=new1
```
