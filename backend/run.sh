#!/bin/bash
[ -z "$PORT" ] &&  PORT=5000
gunicorn --bind 0.0.0.0:$PORT wsgi:app