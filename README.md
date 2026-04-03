# Finance Management System 

This is a Django-based Finance Management System built as part of the Zorvyn task. 
It allows users to track financial records (income and expenses), categorize transactions, and view summaries. The project includes unit tests to ensure data validation and integrity.

## Features

- User registration and authentication(JWT)
- Add income and expense records
- Categorize financial entries
- View transactions by date
- Unit tests for model validation
- 
## User Roles & Permissions

This application has three main roles with distinct access levels:

| Role       | Description | Permissions |
|------------|-------------|-------------|
| **Admin**  | Full control over the system | - Create new users<br>- Add, update, delete financial records<br>- Access Django admin panel |
| **Analyst**| Financial analyst who reviews data | - View financial records (GET requests)<br>- Access reports and summaries<br>- Cannot create, edit, or delete records |
| **Viewer** | User with read-only access | - View financial records only (GET requests)<br>- Cannot access reports or summaries<br>- Cannot create, edit, or delete records |

> **Notes:**  
> - Permissions are enforced through Django authentication and role-based access control.  
> - The main difference between Analyst and Viewer is that Analysts can see **aggregated data or summaries**, while Viewers can only see the raw list of records.


## Technologies Used

- Python 
- Django and DRF
- SQLite (default Django database)
- Django ORM for database management
- unittest (via Django TestCase) for testing

## Installation & Setup

Follow these steps to set up the project locally:

1. Clone the repository
 git clone https://github.com/YogeshBodke21/Zorvyn_task.git

 2. Navigate to the project folder
 cd Zorvyn_task

 3. Create a virtual environment
 python -m venv env

 4. Activate the virtual environment
 Windows:
 env\Scripts\activate
 Linux/Mac: source env/bin/activate

 5. Install dependencies
 pip install -r requirements.txt

 6. Apply database migrations
 python manage.py migrate

 7. Create a superuser (optional, for admin)
 python manage.py createsuperuser

 8. Run the development server
 python manage.py runserver

 9. Access the app in your browser
 http://127.0.0.1:8000/


#Screenshots of Swagger UI

<img width="1707" height="868" alt="image" src="https://github.com/user-attachments/assets/d6451b34-4852-4275-8859-80690af3c6bc" />


<img width="1650" height="859" alt="image" src="https://github.com/user-attachments/assets/f9ac2f03-0564-48d7-9ab6-882a26bc4478" />

#Postman testing -->


<img width="1913" height="955" alt="image" src="https://github.com/user-attachments/assets/b7f30c67-b5da-440d-a2bc-59b34a979281" />


