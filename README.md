## Project Structure:
```bash
flask-app/
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

### How to start application (using Docker)
- Clone the project using command:
    ```
    git clone https://github.com/Rabia23/FlaskProject.git
    ```
- Run the application by the following command:
    ```
    make up
    ```

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
