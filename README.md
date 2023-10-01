# Cart Microservice

This microservice manages shopping cart functionality with status management. \
This project follows froject and app concepts inspired from Django. \
The project name is Cart and the app name is Carts, so in the future we can add other apps and make them seperated. \
You can find more details about how this project was dedigned here: https://medium.com/@khalil.saidane/scalabel-fastapi-project-layered-architecture-10852a40fd38

## Getting Started

These instructions will guide you through setting up and running the Cart microservice locally.

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- [Python 3](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)

### Installation

```bash
# Clone the repository
git clone https://github.com/khalilSaidane/cart.git
cd cart

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install project dependencies using Poetry
source $HOME/.poetry/env
poetry install
```

### Database migrations

```bash
# Navigate to the 'carts' directory 
cd carts

# Create an Alembic migration script
alembic revision -m "Creating cart models" --autogenerate

# Apply the migration to the database
alembic upgrade head
```
### Running the microservice
```bash
# Navigate back to the main directory
cd ..

# Start the Cart microservice using Uvicorn
uvicorn main:app --reload
```

