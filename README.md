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

# Project Structure

- app/: The main application directory.
  - api/: Contains the API routes. Typically organized by version (e.g., v1/) and then by endpoints (e.g., users.py, items.py).
  - core/: Contains the core configuration files like config.py for settings and security.py for authentication logic.
  - models/: Contains the SQLAlchemy models that define the database structure.
  - schemas/: Contains Pydantic models (schemas) used for request and response validation.
  - crud/: Contains CRUD operations encapsulated as functions to interact with the database.
  - db/: Contains database-related files, such as session management (session.py) and base model definitions (base.py).
  - dependencies.py: Contains dependency injection functions used in various routes.
  - main.py: The entry point of the application, where the FastAPI app is instantiated and routes are included.
- tests/: Contains test cases for your application, usually mirroring the structure of the app/ directory.
- alembic/: Directory for database migrations managed by Alembic, with the versions/ subdirectory containing migration scripts.
- .env and .env.example: Environment configuration files for managing secrets and settings. .env.example is a template that others can use to set up their own .env.
- Dockerfile: Contains instructions for building a Docker image of the application.
- requirements.txt: Lists Python dependencies for the project.
- README.md: Documentation about the project.
