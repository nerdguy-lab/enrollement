import os

class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or "secret_string"

    MONGODB_SETTINGS = { 
        "db" : "UTA_Enrollment", #database name
        "host": "localhost", # Or your MongoDB host
        "port": 27017,   # Or your MongoDB port
        "alias": "default",
    }