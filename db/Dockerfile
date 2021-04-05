FROM python:3.8.5
WORKDIR /app/database
COPY . .
RUN apt-get update
RUN apt-get install -y vim
RUN pip install -r requirements.txt
CMD python manage.py runserver 172.20.0.2:8000