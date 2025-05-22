# Django Starter - Ramailo

### Setting up as starter
1. Set the django-starter repo as a starter code to your existing repo
```bash
git remote add starter git@github.com:RamailoTech/django-starter.git
```
2. Pull the django-starter code
```bash
git pull starter main
```
3. Push the code to your repository
```bash
git push origin main
```

### Requirements
1. Make sure you have installed python3 along with venv [Recommended : Python 3.11.4]
[link](https://www.hostinger.com/in/tutorials/how-to-create-a-python-virtual-environment)
3. Setup virtualenv
```
$ python3 -m venv venv
```
3. Activate virtualenv
```
source venv/bin/activate
```

### Run the app in terminal

1. Start a Postgres database on your local machine using docker.
Requirements:
- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
```
make rundb
```

2. Set the values in env.uat as per .env.example file

```
$ make install
$ make createmigrations
$ make migrate
$ make dev
```

### Check if the server is running by visiting the health endpoint

1. Go to [http://localhost:8000/health](http://localhost:8000/health) to see the health of the server.

### Setting up the admin user

1. Setup a password to login to the Django admin dashboard.

```
make adminuser password=<choose-a-secure-password>
```

2. Go to [http://localhost:8000/admin](http://localhost:8000/admin) and login to the dashboard using username `admin` and the password you chose in step 1 above.

### Create a new app

1. Create a new app. Run following from root folder

```
python manage.py startapp [app_name]

```

### Start celery worker, beat and flower

```
$ make worker
$ make beat
$ make flower password=<choose-a-secure-password>
```

### Make API calls against the server

1. Go to [http://localhost:8000/swagger](http://localhost:8000/swagger) to see Swagger documentation for API endpoints.
2. Run the APIs by clicking the "Try it now" button on the Swagger page.

### Run tests and check code coverage

```
$ make test
$ make coverage
```

### Lint your code

```
$ make lint
```

### Watch logs

```
Open logs.log file or console to monitor logs having different log level (e.g., INFO, DEBUG, ERROR).

Log Format: [LEVEL] [TIMESTAMP] [MODULE] [LINE_NUMBER] [MESSAGE]

- LEVEL: Represents the log level of the message, such as "INFO", "DEBUG", "WARNING", etc.
- TIMESTAMP: Represents the timestamp of the log message in the format "YYYY-MM-DD HH:MM:SS,sss".
- MODULE: Represents the name of the Python module where the log message originated.
- LINE_NUMBER: Represents the line number within the Python module where the log message originated.
- MESSAGE: Represents the actual log message content.

Example: [INFO] [2023-07-12 12:34:56,789] [my_module] [42] [This is an example log message]
