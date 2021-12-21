# Airflow setting
## Installation
Please follow the step in the official [website]("https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html").
Here I installed airflow without using constraint (this caused errors) by using the following commend on the website.
```
pip install "apache-airflow[celery]==2.2.2"
```

## Initialize the database
```
airflow db init
```

## Add users
```
airflow users create \
    --username admin \
    --firstname yourfirstname \
    --lastname yourlastname \
    --role Admin \
    --email youremail
```

## Start the web server
**Tip**: default port is 8080

```
airflow webserver -p 8080 -D
```

## Start the schedular

```
# start the scheduler
# open a new terminal or else run webserver with ``-D`` option to run it as a daemon
airflow scheduler

# visit localhost:8080 in the browser and use the admin account you just
# created to login. Enable the example_bash_operator dag in the home page
```

## Stop airflow
```
lsof -i tcp:8080
kill <pid>
```