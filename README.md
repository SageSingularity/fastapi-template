# Fast API Template

A FastAPI template I'm building both to learn and to provide a starting point for projects.

# Quick Start

## Setup Virtual Environment

Before running the project, setup a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/).

Use the virtual environment to manage dependencies, and run the project.

## Install Dependencies

For the `dev` environment:

```
pip install -r ./requirements/dev.txt
```

The `prod` environment is specific to the production environment.

# Run the Project

```
uvicorn src.main:app --reload
```

# Working with PostgreSQL

This template assumes you are using PostgreSQL. To this end, it utilizes [SQLModel](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=postgre).

# Updating Dependencies

Use `pip freeze > requirements/<environment>.txt` to update the dependencies.
