# Getting Started

## Build Project
To build the project, please refer the build guideline.  
https://github.com/Emmeline1101/online-banking-app/blob/main/README.md

## Repository Structure
Here is the basic structure of the bank-app code base.
```graphql
├── README.md                          # Project documentation file with setup instructions and general info.
├── accounts
│   ├── __init__.py                    # Initializes the accounts module, making it a Python package.
│   ├── admin.py                       # Configuration for the admin interface for the accounts models.
│   ├── apps.py                        # Configuration for the accounts application.
│   ├── constants.py                   # Contains constants used within the accounts module.
│   ├── forms.py                       # Defines forms for user input related to account management.
│   ├── managers.py                    # Custom managers for account models, enhancing query capabilities.
│   ├── migrations                     # Directory containing database migrations for the accounts app.
│   │   ├── 0001_initial.py            # First migration file that initializes the database schema.
│   ├── models.py                      # Defines the data models for the accounts application.
│   ├── tests.py                       # Contains tests for the accounts application.
│   ├── urls.py                        # URL declarations for routing in the accounts application.
│   └── views.py                       # View functions that handle requests and responses for the accounts app.
├── banking_system
│   ├── __init__.py                    # Initializes the banking_system module, making it a Python package.
│   ├── asgi.py                        # ASGI config for the project, useful for asynchronous support.
│   ├── celery.py                      # Configures the Celery app for asynchronous task management.
│   ├── settings.py                    # Configuration settings for the Django project (database, middleware, etc.).
│   ├── urls.py                        # The top-level URL route definitions for the entire project.
│   └── wsgi.py                        # WSGI config for the project, used during deployment.
├── celerybeat-schedule.db             # Local database file for storing Celery beat schedule entries.
├── core
│   ├── __init__.py                    # Initializes the core module, making it a Python package.
│   ├── admin.py                       # Admin configurations for core models.
│   ├── apps.py                        # Application configuration for the core app.
│   ├── models.py                      # Defines models related to core functionality of the project.
│   ├── tests.py                       # Tests for the core application.
│   └── views.py                       # Views for handling requests in the core application.
├── db.sqlite3                         # The SQLite database file containing all data for the project.
├── manage.py                          # Command-line utility for administrative tasks.
├── requirements.txt                   # File containing a list of project dependencies.
├── templates                          # Directory containing HTML templates for the project.
│   ├── accounts                       # Templates related to the accounts application.
│   │   ├── user_login.html            # Template for user login page.
│   │   └── user_registration.html     # Template for user registration page.
│   ├── core                           # Core templates used across the application.
│   │   ├── base.html                  # Base template including common elements like header, footer.
│   │   ├── footer.html                # Template for the footer included in base.html.
│   │   ├── index.html                 # Main index or homepage template.
│   │   ├── messages.html              # Template for displaying flash messages.
│   │   └── navbar.html                # Template for navigation bar included in base.html.
│   └── transactions                   # Templates related to the transactions application.
│       ├── transaction_form.html      # Form template for creating transactions.
│       └── transaction_report.html    # Template for displaying transaction reports.
└── transactions
    ├── __init__.py                    # Initializes the transactions module, making it a Python package.
    ├── admin.py                       # Admin configurations for the transactions models.
    ├── apps.py                        # Application configuration for the transactions app.
    ├── constants.py                   # Constants used within the transactions module.
    ├── forms.py                       # Defines forms related to transaction processing.
    ├── migrations                     # Directory for database migrations related to the transactions app.
    │   ├── 0001_initial.py            # Initial migration for the transactions models.
    ├── models.py                      # Data models for managing transactions.
    ├── tasks.py                       # Asynchronous tasks for transactions using Celery.
    ├── tests.py                       # Tests for the transactions application.
    ├── urls.py                        # URL route definitions specific to the transactions app.
    └── views.py                       # Views handling the logic and rendering of transactions.


```
