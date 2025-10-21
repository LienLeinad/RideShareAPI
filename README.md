# Simple Ride Share Dashboard API

## Setup Instructions

Follow these steps to set up and run the application on your local machine:

### 1. Prerequisites
- Python 3.x
- pip

### 2. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/LienLeinad/RideShareAPI.git
cd RideShareAPI
```

### 3. Create a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 4. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 5. Set Up the Database
Run the database migrations to create the necessary tables.
```bash
python manage.py migrate
```

### 6. Create a Superuser
Create an admin account to access the Django admin interface.
```bash
python manage.py createsuperuser
```
You will be prompted to enter a username, email, and password.

### 7. Generate Test Data
The project includes a script to populate the database with sample data.
```bash
python manage.py runscript scripts.generate_test_data
```
You will be prompted to enter the number of iterations to generate data for.

### 8. Run the Development Server
Start the Django development server.
```bash
python manage.py runserver
```

The application will be available at `http://1227.0.0.1:8000/`. You can access the admin panel at `http://127.0.0.1:8000/admin`.

## Usage

1.  **Log In:**
    Navigate to `http://127.0.0.1:8000/login` in your web browser.
    Enter the username and password you created during the `createsuperuser` step.

2.  **View the Ride List API:**
    After a successful login, you will be redirected to the ride list API. This is the main feature of the application, where you can view the created rides generated from the test script.

3. ** Django Debug Toolbar **
    