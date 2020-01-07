## Running the App

### Dependencies:
    Python 3.6.7
    django-cors-headers==3.2.1
    djangorestframework==3.11.0
    drf-nested-routers==0.91
    Node 8.10.0
    NPM 3.5.2

    requirement.txt is also inclued.


## Running the App Locally

### Running the Frontend
    cd frontend
    npm install
    npm start
The app will be live at `localhost:3000`

### Running the Backend
    cd backend
    pipenv install
    pipenv shell
    python manage.py migrate
    python manage.py runserver
The Python app server will be live at `localhost:8000`

### Running the Celery Tasks
    cd backend/kudos
    run in seprate terminal tabs:
        celery -A main worker -l info
        celery -A main beat -l info


NOTES:
- Background task for the kudo count reseting is running every minute right now for testing purpose and can be set to any day of the week from
`setting` variable `DAY_OF_THE_WEEK`


### Data Info
    Dummy data for User, Kudo, Organization are already added
    you can log in with usernames like subham, vedarth with password Root@123