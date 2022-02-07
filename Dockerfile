FROM python:3.8-buster

# set a directory for the app
WORKDIR /usr/src/app
# WORKDIR /Users/peterottsen/training/flask_apps/flask-app-docker

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./app.py"]