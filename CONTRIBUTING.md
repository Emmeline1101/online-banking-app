# Getting Started

## Build Project
To build the project, please refer the build guideline.  
https://github.com/Emmeline1101/online-banking-app/blob/main/README.md

## Repository Structure
Here is the basic structure of the bank-app code base.
```graphql
├── README.md                          # Project documentation file with setup instructions and general info.
├── accounts
│   ├── __init__.py                    
│   ├── admin.py                       
│   ├── apps.py                        
│   ├── constants.py                   
│   ├── forms.py                       # Defines Django forms for user registration
│   ├── managers.py                    # Defines a custom user manager for the Django app
│   ├── migrations                     
│   │   ├── 0001_initial.py            # First migration file that initializes the database schema.
│   ├── models.py                      
│   ├── tests.py                       
│   ├── urls.py                        
│   └── views.py                       # Handle requests and responses for the accounts app.
├── banking_system
│   ├── __init__.py                   
│   ├── asgi.py                        # For asynchronous support.
│   ├── celery.py                      # For asynchronous task management.
│   ├── settings.py                    # A configuration file
│   ├── urls.py                        # Defines the URL routing and mapping various URL paths to corresponding view functions
│   └── wsgi.py                        # Related with deployment.
├── celerybeat-schedule.db             
├── core
│   ├── __init__.py                    
│   ├── admin.py                       # Manage transaction data in Django
│   ├── apps.py                       
│   ├── models.py                      # Record the info of each transaction
│   ├── tests.py                       
│   └── views.py                       # Views for handling requests of the transactions from the frontend
├── db.sqlite3                         # The SQLite database file containing all data for the project.
├── manage.py                          # Entry point for running Django & ensuring Django is properly configured
├── requirements.txt                   # File containing a list of project dependencies.
├── templates                          
│   ├── accounts                       # Templates related to the accounts application.
│   │   ├── user_login.html            
│   │   └── user_registration.html     
│   ├── core                           
│   │   ├── base.html                  # Base template including common elements like header, footer.
│   │   ├── footer.html                
│   │   ├── index.html                 
│   │   ├── messages.html              
│   │   └── navbar.html                
│   └── transactions                   # Templates related to the transactions application.
│       ├── transaction_form.html      
│       └── transaction_report.html    
└── transactions
    ├── __init__.py                   
    ├── admin.py                       
    ├── apps.py                        
    ├── constants.py                   
    ├── forms.py                       
    ├── migrations                     
    │   ├── 0001_initial.py            
    ├── models.py                      
    ├── tasks.py                       
    ├── tests.py                       
    ├── urls.py                        
    └── views.py                      


```
