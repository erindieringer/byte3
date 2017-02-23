"""`main` is the top level module for your Flask application."""

# Mobile Byte Version 1
# 
# Copyright 1/2016 Jennifer Mankoff
#
# Licensed under GPL v3 (http://www.gnu.org/licenses/gpl.html)
#

# Imports
import os
import jinja2
import webapp2
import logging
import json
import urllib
import MySQLdb
import math

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Define your production Cloud SQL instance information.
_INSTANCE_NAME = 'ediering-byte3:us-east1:aware-data'
_DB_NAME = 'aware_data'
_USER = 'ediering' # or hatever other user account you created
_PSWD = 'louise'

# the table where activities are logged
_ACTIVITY = 'plugin_device_usage'
# the table where locations are logged
_LOCATIONS = 'screen'
# the distance that determins new locations
_EPSILON = 1

# Import the Flask Framework
from flask import Flask, request
app = Flask(__name__)

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.
if (os.getenv('SERVER_SOFTWARE') and
    os.getenv('SERVER_SOFTWARE').startswith('Google App Engine/')):
    _DB = MySQLdb.connect(unix_socket='/cloudsql/' + _INSTANCE_NAME, db=_DB_NAME, user=_USER, passwd=_PSWD, charset='utf8')
else:
    _DB = MySQLdb.connect(host='104.196.172.43', port=3306, db=_DB_NAME, user=_USER, passwd=_PSWD, charset='utf8')
    print("error")


@app.route('/')
def index():
    template = JINJA_ENVIRONMENT.get_template('templates/index.html')
    cursor = _DB.cursor()
    cursor.execute('SHOW TABLES')

    query ="select FROM_UNIXTIME(timestamp/1000,'%m-%d-%Y %H:00:00') as 'time', count(*) as 'count' from screen group by time"
    rows = make_query(cursor, query)
    queries2  =[{"query": query, "results": rows}]
    
    #Warning this code is messy I'm so sorry
    #Monday
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 0 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Monday' group by hour"
    rows = make_query(cursor, query)
    queriesM = [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 1 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Monday' group by hour"
    rows = make_query(cursor, query)
    queriesM = queriesM + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 2 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Monday' group by hour"
    rows = make_query(cursor, query)
    queriesM = queriesM + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 3 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Monday' group by hour"
    rows = make_query(cursor, query)
    queriesM = queriesM + [{"query": query, "results": rows}]
    
    #Tuesday
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 0 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Tuesday' group by hour"
    rows = make_query(cursor, query)
    queriesT = [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 1 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Tuesday' group by hour"
    rows = make_query(cursor, query)
    queriesT = queriesT + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 2 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Tuesday' group by hour"
    rows = make_query(cursor, query)
    queriesT = queriesT + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 3 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Tuesday' group by hour"
    rows = make_query(cursor, query)
    queriesT = queriesT + [{"query": query, "results": rows}]
    
    #Wednesday
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 0 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Wednesday' group by hour"
    rows = make_query(cursor, query)
    queriesW = [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 1 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Wednesday' group by hour"
    rows = make_query(cursor, query)
    queriesW = queriesW + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 2 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Wednesday' group by hour"
    rows = make_query(cursor, query)
    queriesW = queriesW + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 3 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Wednesday' group by hour"
    rows = make_query(cursor, query)
    queriesW = queriesW + [{"query": query, "results": rows}]
    
    #Thursday
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 0 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Thursday' group by hour"
    rows = make_query(cursor, query)
    queriesTH = [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 1 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Thursday' group by hour"
    rows = make_query(cursor, query)
    queriesTH = queriesTH + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 2 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Thursday' group by hour"
    rows = make_query(cursor, query)
    queriesTH = queriesTH + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 3 and DAYNAME(FROM_UNIXTIME(timestamp/1000,'%Y-%m-%d')) = 'Thursday' group by hour"
    rows = make_query(cursor, query)
    queriesTH = queriesTH + [{"query": query, "results": rows}]
    
   
    
    
    
    logging.info(cursor.fetchall())
    
    context = {"queries2": queries2, "queriesM": queriesM, "queriesT": queriesT, "queriesW": queriesW, "queriesTH": queriesTH  }
    
    return template.render(context)
    
    
@app.route('/about')
def about():
    template = JINJA_ENVIRONMENT.get_template('templates/about.html')
    
    return template.render()

@app.route('/quality')
def quality():
    template = JINJA_ENVIRONMENT.get_template('templates/quality.html')
    cursor = _DB.cursor()
    cursor.execute('SHOW TABLES')
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 0 group by hour"
    rows = make_query(cursor, query)
    queries = [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 1 group by hour"
    rows = make_query(cursor, query)
    queries = queries + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 2 group by hour"
    rows = make_query(cursor, query)
    queries = queries + [{"query": query, "results": rows}]
    
    query = "select screen_status, Count(*), FROM_UNIXTIME(timestamp/1000,'%H') as 'hour' from screen where screen_status = 3 group by hour"
    rows = make_query(cursor, query)
    queries = queries + [{"query": query, "results": rows}]
    
    context = {"queries": queries }
    
    return template.render(context)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404

@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500

# Takes the database link and the query as input
def make_query(cursor, query):
    # this is for debugging -- comment it out for speed
    # once everything is working

    try:
        # try to run the query
        cursor.execute(query)
        # and return the results
        return cursor.fetchall()
    
    except Exception:
        # if the query failed, log that fact
        logging.info("query making failed")
        logging.info(query)

        # finally, return an empty list of rows 
        return []

# helper function to make a query and print lots of 
# information about it. 
def make_and_print_query(cursor, query, description):
    logging.info(description)
    logging.info(query)
    
    rows = make_query(cursor, query)
        

