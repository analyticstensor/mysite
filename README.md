# Flask Web Application with Login Framework

This repo contains login framework using Python Flask with backend MySQL database.

#### Requirements
1. Install MySQL
 * Create database
2. Set environment variable used in config.py
 * Create config file in user home directory. i.e. .mysite_env
 * Export environment vars with command. export $(grep -v '^#' ~/.mysite_env | xargs)

#### Initialize database
`flask init-db`

#### Run Application
`flask run`

#### Application URL
`http://127.0.0.1:5000/`

