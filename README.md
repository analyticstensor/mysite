# Flask Web Application with Login Framework

This repo contains login framework using Python Flask with backend MySQL database.

## Pre-requisite

1. Install MySQL

    * Create database with specified username and database name specified in environment variable.
    * Login to the console for the database.
      In mysql:      
      ```bash
      $ mysql -u root -p # (Enter your root database password.)
      ```
    Follow below steps:
     1. Create database `mysite` (In mysql)
      ```bash
      mysql> create database if not exists mysite;
      mysql> exit; 
      ```

## Clone Source Code

Clone source code from git repo.

```bash
$ git clone https://github.com/analyticstensor/mysite.git
$ cd mysite
```

You can see list of following files:
```bash
$ ls -1
$ cd mysite
```
_Note list of file display from current folder. LICENSE,README.md,config.py,mysite/,requirements.txt,setup.sh_

### Create and activate virtual environment. Install required packages from requirments.txt

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

    * Install packages from requirements.txt
    ```bash
    pip install -r requirements.txt
    ```

2. Create virtual environment with packages in requirements.txt and activate with `conda`

    ```bash
    $ export sitename=mysite   # Set environment variable for sitename.
    $ conda create --name $sitename --file requirements.txt
    $ conda env list # sitename should be in the list.
    $ conda activate $sitename  # Use recently create environment to create start our web application.
    ```
   Know error for conda:
    * Some of the package need to download from [conda-forge](https://anaconda.org/conda-forge/). Install these package manually: flask-mail==0.9.1, pyjwt==2.4.0, jwt==1.3.1. Following the command below:
    ```bash
    (mysite)$ conda install -c conda-forge pyjwt   # make sure terminal start with virtual environment name. i.e. mysite
    (mysite)$ conda install -c conda-forge flask-mail
    (mysite)$ pip install jwt
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
The above command will prompt. `Creating tables. It has created i.e. user`. 
You can check the information below:
 * Login to database. (i.e. echo $SQLALCHEMY_DATABASE_URI )`mysite` database will be created. 

## Validation

```bash
mysql> use mysite;
mysql> show tables; -- List table: user
mysql> exit;
(mysite)$ echo $sitename # should prompt mysite. if not use command below
(mysite)$ export sitename=mysite   # Set environment variable for sitename.
```

## Run Application

```bash
$ flask run
```

## Checkout application url

`http://127.0.0.1:5000/`

<<<<<<< HEAD
#### Enjoy your application with simple login framework using Python Flask. 

Email us at info@analyticstensor.com for any questions/comments/supports.

=======
#### Enjoy your application with simple login framework using Python Flask. Share the site. Email us at info@analyticstensor.com for any questions/comments/supports.

>>>>>>> 8d4c2440b5518aec189fc7618c742ed7b4ae8361
#### Next to-do list:
 * Add logging
 * Add cookies
 * Add CI/CD pipeline for this site.
