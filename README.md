# PenPal Backend

## Description
This project is a backend service for the PenPal application, built using **FastAPI** and **SQLite**. It provides endpoints for managing tasks, user profiles, authentication, and various other functionalities that support the PenPal application.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User Authentication**: Register, login, and manage user profiles using Firebase.
- **Task Management**: Create, read, update, and delete daily tasks.
- **Calendar Support**: View tasks on a calendar and track completion.
- **Vet Visit Tracking**: Manage pet-related vet visits.
- **Notifications**: (Upcoming) Receive notifications for daily tasks and vet visits.

## Technologies Used
- **FastAPI**: The primary framework for building the API.
- **SQLite**: The database used to store tasks, users, and other relevant data.
- **Firebase**: For handling authentication (sign up, login) and profile management.
- **Uvicorn**: ASGI server for serving the FastAPI application.
- **SQLAlchemy**: For database ORM (Object Relational Mapping) to handle SQLite database.
- **Alembic**: For database migrations.
- **Python**: Backend language.

## Getting Started

### Prerequisites
Make sure you have the following installed on your machine:
- **Python 3.8+**
- **SQLite** (Pre-installed with Python)
- **Pip** (Python package manager)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/penpal-backend.git
    cd penpal-backend
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    # Create a new SQLite database (this will create penpal.db in the app folder)
    alembic upgrade head
    ```

5. Set up your Firebase credentials:
    - Create a Firebase project and download the configuration JSON file.
    - Add the configuration file to the project and update the Firebase authentication settings.

### Running the Application
To run the FastAPI app, use Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

You can also access the auto-generated documentation:
- Swagger UI: `http://127.0.0.1:8000/docs`
- Redoc: `http://127.0.0.1:8000/redoc`

## API Endpoints
Here is a list of the main API endpoints:

- **User Authentication**
  - `POST /auth/register`: Register a new user
  - `POST /auth/login`: Login a user
  - `POST /auth/verify`: Verify a user via email

- **Tasks**
  - `GET /tasks/`: Get all tasks
  - `POST /tasks/`: Create a new task
  - `PUT /tasks/{id}`: Update a task
  - `DELETE /tasks/{id}`: Delete a task

- **Vet Visits**
  - `GET /vet_visits/`: Get all vet visits
  - `POST /vet_visits/`: Add a new vet visit
  - `DELETE /vet_visits/{id}`: Remove a vet visit

## Database Schema

The following tables are used in the SQLite database:

### Users Table
| Column   | Type    | Description           |
|----------|---------|-----------------------|
| id       | Integer | Primary key           |
| name     | String  | User's full name      |
| email    | String  | User's email          |
| password | String  | Hashed password       |

### Tasks Table
| Column     | Type      | Description              |
|------------|-----------|--------------------------|
| id         | Integer   | Primary key              |
| description| String    | Task description         |
| date       | DateTime  | Date task is scheduled   |
| completed  | Boolean   | Task completion status   |
| is_daily   | Boolean   | Marks if it's a daily task|

### Vet Visits Table
| Column   | Type      | Description              |
|----------|-----------|--------------------------|
| id       | Integer   | Primary key              |
| date     | DateTime  | Date of the vet visit    |
| notes    | String    | Notes about the visit    |

## Contributing
We welcome contributions! To contribute:

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some amazing features'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a good foundation for your **PenPal Backend** project, highlighting setup instructions, technology stack, and API structure. You can adapt and expand it as your project evolves!