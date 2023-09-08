    FROM python:3.10.12

    WORKDIR /app

    COPY ./requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .

    CMD ["bash", "-c", "cd /path/to/Neobis_Auth_Project_with_team && python manage.py runserver 0.0.0.0:8000"]
