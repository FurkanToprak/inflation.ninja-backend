#!/bin/sh
gunicorn -b 0.0.0.0:8080 -t 0 app:app