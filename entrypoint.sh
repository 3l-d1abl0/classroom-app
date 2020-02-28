#!/bin/bash

# Apply database migrations
echo "Applying database migrations"

python classroom/manage.py makemigrations classroomapp

python classroom/manage.py migrate

# Start server
echo "Starting server"
python classroom/manage.py runserver 0.0.0.0:8080
