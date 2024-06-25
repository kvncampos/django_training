#!/bin/bash
# This file runs a series of commands using bash shell in Unix-like operating systems.

# 1) Installing dependencies with poetry if it's not installed yet. 
# 2) Navigating to the django_project directory and running Django server.

poetry install || pip install -r requirements.txt
cd django_project/ && python manage.py runserver