__author__ = 'rabia'

# └── dream-team
#     ├── app
#     │   ├── __init__.py
#     │   ├── admin
#     │   │   ├── __init__.py
#     │   │   ├── forms.py
#     │   │   └── views.py
#     │   ├── auth
#     │   │   ├── __init__.py
#     │   │   ├── forms.py
#     │   │   └── views.py
#     │   ├── home
#     │   │   ├── __init__.py
#     │   │   └── views.py
#     │   ├── models.py
#     │   ├── static
#     │   └── templates
#     ├── config.py
#     ├── instance
#     │   └── config.py
#     ├── migrations
#     │   ├── README
#     │   ├── alembic.ini
#     │   ├── env.py
#     │   ├── script.py.mako
#     │   └── versions
#     │       └── a1a1d8b30202_.py
#     ├── requirements.txt
#     └── run.py
from app import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)


if __name__ == '__main__':
    app.run()
