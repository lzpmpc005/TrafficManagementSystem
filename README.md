# Django Traffic Management Project

This Django project aims to provide a solution for traffic management by implementing various features using Django and MySQL.

## Description

This project use Django, along with MySQL as the database backend to create a web application for managing traffic-related data.

## Features

* **User Service**: Provides user authentication and management functionalities.
* **Notifications**: Allows sending notifications to users about traffic-related events.
* **Database Backend**: Uses MySQL for storing application data.

## Requirements

1. For Mac OS

    * Python 3.11.5
    * Django 4.2.6
    * MySQL 8.2.0 arm-64
2. For Windows you can refer to Mac OS

## Preparation

1. Install packages (see Installation)
2. (Very important!) Install and make sure your MySQL server works properly, here are some tutorials and resources

    * Tutorial to install MySQL server and visualization database controlling platform

      https://www.youtube.com/watch?v=7S_tz1z_5bA&t=65s
    * Tutorial to connect Django and MySQL server

      https://studygyaan.com/django/how-to-use-mysql-database-with-django-project

      https://www.youtube.com/watch?v=SNyCV8vOr-g&t=49s
    * If you have problem on mac when installing MySQL client in python

      https://stackoverflow.com/questions/66669728/trouble-installing-mysql-client-on-mac

## Installation

1. Clone the repository
2. Navigate to the project directory:

    ```bash
    cd Traffic_Management
    ```
3. Install dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```
4. If you don't want to install all the libraries the same as the contributors, here are some core libraries:
    Copy, paste and cover them in requirements.txt and repeat step 3, but error may happen due to system differences

    ```
    Django==4.2.6
    django-cors-headers==4.3.1
    django-extensions==3.2.3
    django-filter==23.3
    djangorestframework==3.14.0

    mysql-connector-python==8.3.0
    mysqlclient==2.2.1

    Faker==22.5.1
    ```
5. Configure the database settings in `Traffic_Management/settings.py` according to you database setting:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_mysql_database',
            'USER': 'your_mysql_username',
            'PASSWORD': 'your_mysql_password',
            'HOST': 'localhost', # modify it if yours are different
            'PORT': '3306', # modify it if yours are different
        }
    }
    ```
6. Apply database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Notes for Usage

1. (highly recommanded!) Import SQL script provided (see file in repository) for initial data

    if you don't know how to import SQL script please search according to the database application you use
2. Generate data by in-built functions

    (data to be added soon)
3. Use the provided REST API endpoints for interacting with the application programmatically.
4. (very important!) When use built-in functions read from external resources otherthan database, check the file_path variables! 
5. (highly recommanded!) Use Postman to test REST API endpoints

    if you don't know how to use Postman go to: https://www.postman.com/

    * example 1 (to be built)
6. Use Terminal to test REST API endpoints

    if you don't know how to use Terminal search on Google for "how to use terminal to send request" or something alike

    * example 1 (to be built)
  
## Senarios and usages 
(still building)
1. Implementing Vehicle Registration and License Plate Recognition
   1.1 Register
   1.2 Recognize
2. Monitoring Traffic Violations and Issuing Fines
   2.1 Detect violation
   2.2 Issue fines
3. Analysing Traffic Flow and Managing Congestion
   3.1 Analyse flow
      3.1.1 implement Traffic_Management/User_Service/detection_monitor_streets_v2.py
      3.1.2 implement Traffic_Management/User_Service/predict_traffictime_nextday_v2.py
      3.1.3 the 'detection_monitor_streets' will produce simulated data and 'predict_traffictime_nextday' will analyse it
      3.1.4 the output will be a conclusion about busiest hour and a list of total average flow per hour
   3.2 Notify drivers
      3.2.1 go to Traffic_Management/Notification/flow_visualization.py
         3.2.1.1 change the 'folder_name' according to your senarios (or set default if using the given data package)
         3.2.1.2 implement Traffic_Management/Notification/flow_visualization.py
      3.2.2 the 'flow_visualization' will plot a graphic according to the output of 'predict_traffictime_nextday'
      3.2.3 run the server for the following instructions
         3.2.3.1 open terminal or postman (see 'Notes for Usage' about how to use)
         3.2.3.2 to use default URL: http://localhost:8000/notification/send_congestion_warning/2024-02-06/London/
         3.2.3.3 to customize URL according your senario here is the template: http://localhost:8000/notification/send_congestion_warning/<str:formatted_date>/<str:fake_city>/
         3.2.3.4 go to the main dialect and go to setting.py
            3.2.3.4.1 search for EMAIL_HOST and modify it according to yours (default is Gmail)
            3.2.3.4.2 see tutorials like this: https://stackoverflow.com/questions/6367014/how-to-send-email-via-django
            3.2.3.4.3 the setting of EMAIL_HOST is very trick according to what service you use
            3.2.3.4.4 to modify the receiver
               3.2.3.4.4.1 open your database and the table Driver
               3.2.3.4.4.2 add yourself as a driver and make should the email address is valid
               3.2.3.4.4.3 go to 'Notification/User_Service'
               3.2.3.4.4.4 find 'drivers = Driver.objects.filter(driverName="Charton")'
               3.2.3.4.4.5 replace 'Charton' to your name (should be same as the name you input in database the 1st step)
         3.2.3.4 use the method GET to test
4. Prioritising Emergency Vehicles and Clearing Routes
         

## Contributing

Contributions are welcome!
