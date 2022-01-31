FROM python:3.8-buster

WORKDIR /Users/peterottsen/training/flask_apps/flask-app-docker

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

# CMD ["export", "FLASK_APP=app;", "flask", "run"]
CMD ["python", "./app.py"]