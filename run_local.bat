@echo off
call venv\Scripts\activate
set FLASK_APP=app\main.py
flask run
