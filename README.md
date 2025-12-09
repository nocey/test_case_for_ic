
# IC Holding Test Case 🚀

This repository contains the source code for the IC Holding Test Case project. Follow the instructions below to set up the development environment, configure the database, and run the application.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:

-   **Python 3.x**
    
-   **Docker** & **Docker Compose**
    
-   **Git**
    

## Installation & Setup

Follow these steps to get the project running locally.

### 1. Create and Activate Virtual Environment

It is recommended to create a dedicated virtual environment (`venv`) to manage dependencies.

**macOS / Linux:**

```
# Create the virtual environment named 'venv'
python3 -m venv venv

# Activate the environment
source venv/bin/activate

```

**Windows:**

```
# Create the virtual environment
python -m venv venv

# Activate the environment
.\venv\Scripts\activate

```

### 2. Install Dependencies

Once the virtual environment is active, install the required Python libraries.

```
pip install -r requirements.txt

```

### 3. Environment Configuration 

Before starting the database, ensure your environment variables are set correctly.

-   Check the `.env` file (or create one if it doesn't exist).
    
-   **Note:** If the default PostgreSQL port (`5432`) is already in use on your machine, you must update the port mapping in the `docker-compose.yml` or your `.env` file to avoid conflicts.

    

### 4. Initialize Database (Docker)

Start the PostgreSQL database container using Docker Compose.

```
docker compose up -d

```

### 5. Run Migrations

Apply the database migrations to set up the schema in the newly created PostgreSQL container.

```
python manage.py migrate

```

### 6. Start the Development Server

Finally, run the Django development server.

```
python manage.py runserver

```

The application should now be accessible at `http://127.0.0.1:8000/`.
