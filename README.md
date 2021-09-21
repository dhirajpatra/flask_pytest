# simple application to use pytest with flask

This application created from a tutorial. I have shared here to use as a template for flask and pytest.

## how to run

Open a termincal and run

`python blog/init_db.py`
`FLASK_APP=blog/app.py python -m flask run`

open another terminal and run the tests

`python -m pytest tests`

or

`python -m pytest tests -m 'e2e'`
