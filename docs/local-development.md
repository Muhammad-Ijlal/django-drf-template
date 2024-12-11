## Running project locally

### Preparing environment
Before running the application, make sure all dependencies are installed.
This step can be skipped, if you are going to run the project in the docker environment.

#### Python environment
Create and activate virtualenv to isolate all used packages for the service:
```bash
python3 -m venv venv
. venv/bin/activate
```

#### Backing services
Make sure next services are up and running to be able to run the app:
Make sure to create database, which will be used in the application:
  ```sql
  create database <database_name>;
  ```
This can be run directly on the system or run as docker containers.

### Installing requirements
Install all Python packages, required to run the application:
```bash
pip install -r requirements.txt
```

### Configuring

#### Providing settings
Most of the configurations are expected to be provided as environment variables.
It is possible to provide all variables in the `.env` file, located in the root of the project.
Please refer to [sample .env.example](../.env.example) file for reference.
Additionally, provide module to be used as main django configs entry point: `DJANGO_SETTINGS_MODULE=config.settings.development`.

#### Installing pre-commit hooks
```bash
pre-commit install
```

#### Applying migrations
```bash
python manage.py migrate
```

### Running application directly
```bash
python manage.py runserver 0.0.0.0:8000
```

### Running inside docker environment
There is a [docker-compose](../docker-compose.yaml) file, which can be used to run services locally.
```bash
docker-compose up -d
```

### Testing
Tests are written using `pytest` library.
Each nested applications in the `apps` folder contain tests, isolated for that specific application.
Tests execute on isolated database, which tears down after tests finish.
To execute tests, run following command (assuming virtualenv is activated):
```bash
python -m pytest
```