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
    
    <img width="658" height="236" alt="image" src="https://github.com/user-attachments/assets/061805df-d607-4bc2-a552-9f67b859142a" />


3.  **View the Ride List API:**
    After a successful login, you will be redirected to the ride list API. This is the main feature of the application, where you can view the created rides generated from the test script.
    
    <img width="1594" height="828" alt="image" src="https://github.com/user-attachments/assets/c0ecd00a-ba75-426e-8043-42ea929a6345" />


5. ** Django Debug Toolbar **
   If it did not already show up on the screen, click the Django Debug Toolbar Side button to reveal the debug panel. This will help show how many queries are made in the API request
   
    <img width="229" height="159" alt="image" src="https://github.com/user-attachments/assets/e9c17cdf-5ff5-4878-a5a4-a26a9cb4bb33" />
    <img width="408" height="697" alt="image" src="https://github.com/user-attachments/assets/7c6560ef-861b-4276-9b7b-1ed4d01853aa" />

    Clicking the SQL tab will explain what queries were made in better detail.
   
   <img width="1606" height="383" alt="image" src="https://github.com/user-attachments/assets/331091f0-5b30-4844-9323-e368447997fe" />
   
    The first two queries made are necessary authentication queries, to ensure that the user in the request is authenticated
    The next three queries are what make up the results of the API request. The first being a count of all the results from the Ride List API.
    The next being a query to retrieve the first 20 rides in the database alongside their respective Rider and Driver information
    The last query is a query to retrieve the associated ride events of each of the rides given in the prior query.
7. ** Filters and Ordering **

    Filtering can be done via Query Parameters in the URL or in the browsable API page rendered by django rest framework.

    ### Ordering by pickup time
   
    <img width="732" height="358" alt="image" src="https://github.com/user-attachments/assets/462a0f58-e08f-4ed0-84ae-89b32ddb3826" />

    ### Filtering by rider email
   
    The test data generation script will generate random string emails, you can choose any from the ride list API and plug it in the search filter
   
    <img width="717" height="81" alt="image" src="https://github.com/user-attachments/assets/227ab634-2adb-4569-99f1-8916ca22b00c" />

    ### Filtering by Ride Status
   
    <img width="736" height="97" alt="image" src="https://github.com/user-attachments/assets/0a9c696a-6730-4608-97ca-6f7a5ba74bcb" />

    
