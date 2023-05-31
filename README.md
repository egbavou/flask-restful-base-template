# flask-restful-base-template

This project shows one of the possible ways to implement RESTful API server.

Main libraries used:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.
4. Flask-SQLAlchemy - adds support for SQLAlchemy ORM.

Project structure:
```
.
├── app
│   ├── __init__.py
│   ├── exceptions
│   │   ├── __init__.py
│   │   └── handler.py
│   ├── http
│   │   ├── controllers
│   │   │   ├──__init__.py
│   │   ├── requests
│   │   │   ├──__init__.py
│   │   └── resources
│   │      ├──__init__.py
│   ├── mail
│   │   └── __init__.py
│   ├── models
│   │   └──  __init__.py
│   ├── rules
│   │   └── __init__.py
│   └── utils
│       ├── __init__.py
│       ├── common.py
│       ├── http_code.py
│       └── logz.py
├── .env
├── .env.example
├── .gitignore
├── api.py
├── config.py
├── db.py
├── README.md
├── requirements.txt
└── routes.py
```

## Running 

1. Clone repository.
2. Run following commands:
    1. cd myproject
    2. python3 -m venv .venv
    2. . .venv/bin/activate
    3. pip install -r requirements.txt
    4. python3 api.py