# play - Full Stack Web Application

This is a simple full-stack web application built using Django for managing a list of stocks. The application allows users to Create, Read, Update, and Delete (CRUD) stock entries, with each stock having a name, ticker symbol, and price. The backend is built using Django REST Framework and PostgreSQL as the database, while the frontend uses HTML, CSS (Bootstrap), and JavaScript to provide a functional and interactive interface.

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [API Endpoints](#api-endpoints)
- [File Structure](#file-structure)
- [How to Use](#how-to-use)

## Features

- Add new stocks with name, ticker symbol, and price.
- View a list of all stocks.
- Update the details of an existing stock.
- Delete stocks from the list.
- Input validation to ensure correct data entry.
- Basic pagination (if implemented).
- Styled with Bootstrap for a clean and responsive UI.

## Screenshot
![Stock Manager Screenshot](./stock_manager.png)

## Technologies Used

**Backend:**

- Framework: Django (with Django REST Framework)
- Database: PostgreSQL
- Language: Python

**Frontend:**

- HTML5, CSS3 (Bootstrap), JavaScript
- AJAX for dynamic updates

## Requirements

Before running the project, ensure you have the following installed:

- Python
- PostgreSQL
- Django
- Django REST Framework
- Bootstrap (loaded via CDN in the HTML)

## Installation & Setup

Follow these steps to set up and run the project on your local machine.

1. **Clone the Repository**
    ```bash
    git clone https://github.com/aslammiya/stocks-manager
    cd stocks-manager
    ```

2. **Activate Virtual Environment**

   **On macOS/Linux:**
     ```bash
     source env/bin/activate
     ```
   **On Windows:**
     ```cmd
     .\env\Scripts\activate
     ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure PostgreSQL Database**

    Ensure PostgreSQL is installed and running on your machine.
    Create a PostgreSQL database:
    ```bash
    CREATE DATABASE stocks;
    CREATE USER postgres WITH PASSWORD '123456';  # Ensure these match your settings
    ALTER ROLE postgres SET client_encoding TO 'utf8';
    ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';
    ALTER ROLE postgres SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE stocks TO postgres;

    ```
    Update the DATABASES setting in settings.py to reflect your PostgreSQL settings:
    ```bash
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'stocks',
                'USER': 'postgres',
                'PASSWORD': '123456',
                'HOST': 'localhost',
                'PORT': '5432',
            }
        }
    ```

5. **Run Migrations**
```bash
    python manage.py makemigrations

    python manage.py migrate
```

6. **Run the Development Server**
```bash
    python manage.py runserver
```

## API Endpoints
- `GET /stocks/`: Retrieve all stocks
- `POST /stocks/`: Create a new stock.
- `GET /stocks/<id>/`: Retrieve a specific stock by ID.
- `PUT /stocks/<id>/`: Update a specific stock by ID.
- `DELETE /stocks/<id>/`: Delete a specific stock by ID.

## Frontend
The frontend provides a simple interface for interacting with the stock data:

- **Stock List**: Displays all stocks and their details (name, ticker symbol, price).
- **Add Stock**: A form that allows users to add a new stock.
- **Edit Stock**: Allows users to update stock details.
- **Delete Stock**: Allows users to remove a stock from the list.

The frontend interacts with the backend API using AJAX to provide a seamless user experience.

## File Structure
```
├── stocks/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # Stock model with name, ticker_symbol, price fields
│   ├── serializers.py       # Serializes stock data for the API
│   ├── views.py             # Contains stock CRUD API views
│   └── urls.py              # URL routes for the API endpoints
├── templates/
│   └── index.html           # Frontend template for managing stocks
├── core/
│   ├── settings.py          # Django settings (includes DB config)
│   └── urls.py              # Main URL routing
└── manage.py                # Django management command
```

## How to Use
- **Add a Stock**: Use the form on the homepage to add a new stock. Enter the stock name, ticker symbol, and price, then click "Add Stock".
- **View Stocks**: The stock list will automatically update to display all added stocks.
- **Update a Stock**: Click the "Update" button next to a stock entry to open a modal form. Modify the stock details and submit the changes.
- **Delete a Stock**: Click the "Delete" button next to a stock to remove it from the list.