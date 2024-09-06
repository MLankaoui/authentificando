# authenficando
- A simple auth system using django and mysql

## How to setup

1. clone the repo:
```bash
    git clone https://github.com/MLankaoui/authentificando
    cd authentificando
```

2. create a virtual environemnt:
- for linux:
```bash
    python3 -m venv venv
```
- for window:
```bash
    python -m venv venv
```

3. run the virtual environemnt:

4. install all requirements:
```bash
    pip install -r requirements.txt
```

5. do migrations:
```bash
    python manage.py migrate
```

6. create a superuser
```bash
    python manage.py createsuperuser
```

enjoy.