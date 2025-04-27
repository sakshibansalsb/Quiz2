# Quiz2 - Employee Management System

A Django REST Framework based web application to manage synthetic employee data.

## Features

- Employee, Department, Attendance, and Performance models
- Data generation using Faker
- REST APIs (CRUD operations)
- SQLite database (local, no external setup)
- Swagger UI for API documentation
- Token Authentication
- Health Check endpoint
- Admin panel access
- API rate limiting

## Project Structure

Quiz2/
├── manage.py
├── requirements.txt
├── README.md
├── Quiz2/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── employee_app/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── management/
│   │   └── commands/
│   │       └── generate_employees.py
│   └── templates/
│       └── charts.html
└── db.sqlite3 (after migration)

## Installation & Running

1. Open terminal inside Quiz2 project directory.

2. Create and activate a virtual environment:
    - Windows:
      ```
      python -m venv venv
      venv\Scripts\activate
      ```
    - macOS/Linux:
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Make migrations for your app:
    ```
    python manage.py makemigrations employee_app
    ```

5. Apply migrations:
    ```
    python manage.py migrate
    ```

6. Create a superuser:
    ```
    python manage.py createsuperuser
    ```

7. Generate sample employee data:
    ```
    python manage.py generate_employees
    ```

8. Run the development server:
    ```
    python manage.py runserver
    ```

## Access the App

- Django Admin: http://127.0.0.1:8000/admin/
- Swagger UI: http://127.0.0.1:8000/swagger/
- Health Check: http://127.0.0.1:8000/health/
- Employees API: http://127.0.0.1:8000/api/employees/

## API Endpoints

- `GET /api/employees/`
- `POST /api/employees/`
- `GET /api/attendances/`
- `POST /api/attendances/`
- `GET /api/performances/`
- `POST /api/performances/`
- `GET /api/departments/`
- `POST /api/departments/`
- `POST /api/token-auth/` (get authentication token)

## Notes

- SQLite database is used for easy setup.
- Faker library is used for data generation.
- Rate limiting: 1000 API calls per user per day.
- Token Authentication is enabled for API access.

