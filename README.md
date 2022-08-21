# Flask Web Application with Login Framework

This repo contains login framework using Python Flask with backend MySQL database.

## Pre-requisite

1. Install MySQL

    * Create database with specified username and database name specified in environment variable.

## Clone Source Code

Clone source code from git repo.

```bash
$ git clone https://github.com/analyticstensor/mysite.git
$ cd mysite
```

### Create and activate virtual environment

1. Create virtual environment with `venv`

   ```bash
   $ python -m venv myenv # create virtual env    
   ```

    * Activate virtual environment in Window

    ```bash
    $ myenv\Scripts\activate.bat
    ```

    * Activate virtual environment in Unix/MacOS

    ```bash
    $ source myenv/bin/activate
    ```

2. Create virtual environment and activate with `conda`

    ```bash
    $ sitename=mysite
    $ conda create --name $sitename --file requirements.txt
    $ conda activate $sitename
    ```

## Set environment variable used in config.py

  Create config file in user home directory. i.e. ~/.mysite_env. Sample .mysite_env file.
  
  ```bash
  FLASK_APP='mysite'
  FLASK_ENV='development'
  SECRET_KEY='my_secret_key'
  SQLALCHEMY_DATABASE_URI='mysql+mysqldb://dbusername:dbpassword@localhost/dbname'
  MAIL_SERVER='mailservername'
  MAIL_PORT='465'
  MAIL_USE_SSL='True'
  MAIL_USERNAME='email@mysite.com'
  MAIL_PASSWORD='password'
  MAIL_SENDER='email@mysite.com'
  ```
  
  Set environment variable from ~/.mysite_env file.

  ```bash
$ export $(grep -v '^#' ~/.mysite_env | xargs)
  ```
  
## Initialize database

```bash
$ cd mysite
$ flask init-db
```

## Run Application

```bash
$ flask run
```

## Checkout application url

`http://127.0.0.1:5000/`
