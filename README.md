# VIRTUAL LIBRARY

Welcome to Alexandria. This virtual library is a project destined for me to learn about best practices and slowly get into clean code and clean architecture.

## Usage

This asumes:

    - You have installed the requirements.
    - You have Docker installed and running.

\#1: Run (to get the mysql latest image from docker's repo):
```
docker pull mysql
```

\#2: Run (to run the container based on that image):
```
docker run --name mysql-container -e MYSQL_ROOT_PASSWORD=mysql12345-d mysql
```


\#3.1: With the container running, now you have a database to store results and to query about. Now you just need an easy way of interacting with it. To run the FastAPI docs:
```
uvicorn --reload back.main:app
```
After running that command, go to http://127.0.0.1:8000/

<br>

\#3.2: To check the front, run these two commands:
```
cd front
npm run serve
```
After running that command, go to http://127.0.0.1:8080/
