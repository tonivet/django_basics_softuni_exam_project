# Management of Income and Expenses for Condominium Properties

## Description

This project is a Django web application designed to facilitate the management of income and expenses in condominium properties (apartment buildings, residential complexes, etc.). It allows administrators to add, edit, and view income and expenses, generate reports, and maintain an overview of the building's financial status. Maintaining condominium record book, incoming and outgoing correspondence, and a bulletin board.

## Features

* **Create a condominium property**
  * From django admin add address, number of apartments, percentage of ideal parts.
* **User Management:**
  * From Django admin create and manage user accounts with different access levels'
* **Condominium register**
  * Add, edit or delete owners, residents, tenants, pets. Filter them by category, search through first or last name. 
* **Condominium bulletin board**
  * Add, edit or delete notes from the board. Filter them by status.
* **Condominium record book**
  * Add invoices for payments, mails to condominium from institutions, scanned protocols from general meetings, download or delete them.
* **Management of income and expenses**
  * under development


## Requirements

* **Python:** 3.8 or newer
* **Django:** 4.0 or newer
* **PostgreSQL** 
* **Django Debug Toolbar** if you don't want to use it, you'll have to remove it form installed apps in settings.py
* **environ** if you want to use different app to import env variables, you should remove it form settings.py


## Environment variables
Open .env.template file and add the values ​​of the required variables. Rename the file to .env

## Installation

1. **Clone the repository:**

    ```bash
    git clone [Repository URL]
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    * Create a PostgreSQL database (if using PostgreSQL).
    * Open `settings.py` and update the database settings (`DATABASES`).

5. **Migrate the database:**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

## Running the application

```bash
python manage.py runserver
```

## License

MIT License or Apache License 2.0