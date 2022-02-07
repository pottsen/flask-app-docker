# flask-app-docker

Used this tutorial to get started and learn docker:
https://docker-curriculum.com/

Using Colima instead of docker desktop as containter runtime.
https://github.com/abiosoft/colima

### 01/31/2022
Had issues getting my own app exposed.
Trying to just get the basic 'Hello World' functionality running from a prior app I built.

### 02/01/2022
#### Potential Issues:
- Requirements file -- (NOT THE ISSUE)
- Potentially the path in the Dockerfile -- (NOT THE ISSUE) (Should this path be the path in the container?)
- app.run in app.py -- (SWAPPED TO SAME FROM TURORIAL AND IT WORKED)

`if __name__ == '__main__':
    # USE THIS ONE
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))'

It's the 0.0.0.0... basically a networking thing. Explanation here in the "Externally Visible Server" section: https://flask.palletsprojects.com/en/2.0.x/quickstart/
the "virtual server" running docker get's it's own IP address and flask runs within it. So by default, only other stuff running in that docker container could talk to flask
the host=0.0.0.0 allows flask to listen to connections coming in from anywhere.

The app will be exposed on http://localhost:8888/
