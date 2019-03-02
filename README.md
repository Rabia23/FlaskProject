## Summary:
The REST APIs are built using Python Flask framework. Docker containers are used for development environment.

It contains the below mentioned endpoints:
- a POST '/grab_and_save'
- a GET '/last'

There are many ways to setup your project folder structure. One is by its function and another is app based structure which means things are grouped bp application. I have used app based approach for this task.

## Project Structure (App Based):
```bash
FlaskProject/
├── Dockerfile
├── Makefile
├── README.md
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── resources.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── constants.py
│   ├── db.py
│   ├── settings.py
│   └── utils.py
├── config.py
├── docker-compose.yml
├── entrypoint.sh
├── migrate.py
├── migrations/
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── .gitignore
├── requirements.txt
└── run.py
```

### Python extensions used:
- **flask** - This is a microframework for Python
- **flask_restful** - This is an extension for Flask that adds support for quickly building of REST APIs.
- **flask_script** - This is an extension that provides support for writing external scripts in Flask.
- **flask_migrate** - This is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
- **flask_sqlalchemy** - This is an extension for Flask that adds support for SQLAlchemy. It allows to write ORM queries to operate against database.
- **flask_marshmallow** - This is an integration layer for Flask and marshmallow (ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes. This is used also to Serializing and Deserializing Objects.) that adds additional features to marshmallow.
- **mysqlclient** - MySQL database connector for Python
- **requests** - This is a python library to make calls to external APIs

### How to start application (using Docker)
- Clone the project using command:
    ```
    git clone https://github.com/Rabia23/FlaskProject.git
    ```
- Go into the project directory:
    ```
    cd flask-application
    ```
- Run the application by the following command:
    ```
    make up
    ```

### How to ssh into a Docker containers
- ssh into app container
    ```
    make app-shell
    ```
- ssh into database container
    ```
    make db-shell
    root@e27d5a54fbb8:/# mysql -u root -p
    Enter password: root
    mysql> show databases;
    mysql> use testdb;
    mysql> show tables;
    mysql> select * from wallets;
    ````

### Test using CURL
- curl -H "Content-Type: application/json" -X POST -d '{"currency_code": "AED", "requested_amount": 19.7654}' http://127.0.0.1:5000/api/grab_and_save
    ```
    {"message": "Data successfully saved", "response": {"requested_amount": 19.7654, "currency_code": "AED", "created_on":  "2019-02-05T11:10:58+00:00", "id": 4, "updated_on": "2019-02-05T11:10:58+00:00", "open_exchange_price": 3.67328, "final_amount": 72.6039}, "success": true}
    ```
- curl -H "Content-Type: application/json" -X POST -d '{"requested_amount": 19.7654}' http://127.0.0.1:5000/api/grab_and_save
    ```
    {"message": "Params are missing", "response": {}, "success": true}
    ```
- curl -H "Content-Type: application/json" -X POST -d '{"currency_code": "AED", "requested_amount": -0.34567309}' http://127.0.0.1:5000/api/grab_and_save
    ```
    {"message": "Invalid data", "response": {}, "success": true}
    ```
- curl -X GET http://127.0.0.1:5000/api/last
    ```
    {"message": null, "response": {"requested_amount": 19.7654, "currency_code": "AED", "created_on": "2019-02-05T11:10:58+00:00", "id": 4, "updated_on": "2019-02-05T11:10:58+00:00", "open_exchange_price": 3.67328, "final_amount": 72.6039}, "success": true}
    ```
- curl -X GET "http://127.0.0.1:5000/api/last?no_of_operations=3"
    ```
    {"message": null, "response": [{"requested_amount": 19.7654, "currency_code": "AED", "created_on": "2019-02-05T11:10:58+00:00", "id": 4, "updated_on": "2019-02-05T11:10:58+00:00", "open_exchange_price": 3.67328, "final_amount": 72.6039}, {"requested_amount": 19.7654, "currency_code": "AED", "created_on": "2019-02-05T10:18:42+00:00", "id": 3, "updated_on": "2019-02-05T10:18:42+00:00", "open_exchange_price": 3.67316, "final_amount": 72.6014}, {"requested_amount": 19.7654, "currency_code": "AED", "created_on": "2019-02-05T09:21:50+00:00", "id": 2, "updated_on": "2019-02-05T09:21:50+00:00", "open_exchange_price": 3.67316, "final_amount": 72.6014}], "success": true}
    ```
- curl -X GET "http://127.0.0.1:5000/api/last?currency_code=ALL"
    ```
    {"message": null, "response": {"requested_amount": 11.9854, "currency_code": "ALL", "created_on": "2019-02-05T09:21:04+00:00", "id": 1, "updated_on": "2019-02-05T09:21:04+00:00", "open_exchange_price": 109.15, "final_amount": 1308.21}, "success": true}
    ```
 - curl -X GET "http://127.0.0.1:5000/api/last?currency_code=AED&no_of_operations=2"
    ```
    {"message": null, "response": [{"requested_amount": 19.7654, "currency_code": "AED", "created_on": "2019-02-05T11:10:58+00:00", "id": 4, "updated_on": "2019-02-05T11:10:58+00:00", "open_exchange_price": 3.67328, "final_amount": 72.6039}, {"requested_amount": 19.7654, "currency_code": "AED", "created_on": "2019-02-05T10:18:42+00:00", "id": 3, "updated_on": "2019-02-05T10:18:42+00:00", "open_exchange_price": 3.67316, "final_amount": 72.6014}], "success": true}
    ```
 - curl -X GET "http://127.0.0.1:5000/api/last?currency_code=AFB"
    ```
    {"success": true, "response": {}, "message": "Does Not Exists"}
    ```
