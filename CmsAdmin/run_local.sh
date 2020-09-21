#!/bin/bash

export `cat config/envs/local.env`
python manage.py runserver