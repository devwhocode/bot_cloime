# database.py
import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT

def connect_to_remote_db():
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, db=DB_NAME, port=DB_PORT, charset='utf8')
    return connection