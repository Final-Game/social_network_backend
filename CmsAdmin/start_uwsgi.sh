#!/bin/sh

gunicorn CmsAdmin.wsgi:application --bind 0.0.0.0:8000 --workers=4