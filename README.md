# Gudlift-registration

An app that allows power-lifting clubs to register in competitions.

Using Flask, the goal of the project is to develop the phase 2 of the code available at https://github.com/OpenClassrooms-Student-Center/Python_Testing


## The structure

Each bug and error has been corrected in its own branch.

The finished code and tests (units, functionnal and performance) are available in the QA branch.


## Prerequisites and using the application

1. Install Python 3

2. Unzip the files from the QA branch in your desired folder

3. Install the app 

- Change to this directory and install venv by typing in your terminal :
```
pip install venv
```
- Create de the virtual environement and launch it by typing :
```
python -m venv env
```
and
```
env\Scripts\activate
```
- install moduls and packages by typing :
```
pip install -r requirements.txt
```


3. Launch the Flask server
```
set FLASK_APP=server.py
```
and
```
flask run
```

You can access the website through your browser at http://127.0.0.1:5000/
You can use it using the data contained in clubs.json 


## Testing

1. Unit and functionnal tests can be run using pytest, using the following command :
```
pytest
```

You can generate coverage reports to htmlcov directory by typing :
```
pytest --cov=. --cov-report html
```

2. Performance tests are executed using Locust. Type in :
```
locust -f tests\performance_tests\locustfile.py --web-host localhost
```

Access http://localhost:8089 through your browser, choose 6 users, enter http://127.0.0.1:5000 as host and start the test.
