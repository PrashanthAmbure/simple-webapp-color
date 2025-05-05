FROM python:latest

WORKDIR /opt/apps/simple-webapp-color

COPY . /opt/apps/simple-webapp-color

RUN pip install flask

CMD ["python", "app.py"]