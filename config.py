import os

class Config(object):
    SECRET_KEY =os.environ.get('SECRET_KEY') or b'\xe9\xd0H\x9b)6\x8dA+\xea \x10a\xbc\x1f8'

    MONGODB_SETTINGS = { 
        "db" : "UTA_Enrollment", #database name
        "host": "localhost", # Or your MongoDB host
        "port": 27017,   # Or your MongoDB port
        "alias": "default",
    }