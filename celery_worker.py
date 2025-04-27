"""This is the file called when initializing the worker"""
from factories.app import create_app
from factories.celery import configure_celery

# Imported for type hinting
from flask import Flask
from celery import Celery

app: Flask = create_app()
celery: Celery = configure_celery(app)