import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()


def open_database():

    try:
        connection = mysql.connector.connect(host=os.environ.get('MYSQL_HOST'),
                                             user=os.environ.get('MYSQL_USER_NAME'),
                                             passwd=os.environ.get('MYSQL_PASSWORD'),
                                             db=os.environ.get('MYSQL_DB_NAME'))
    except Error as e:
        print("Error while connection to MySQL", e)
    return connection


def connection_handler(function):
    def wrapper(*args, **kwargs):
        connection = open_database()
        dict_cur = connection.cursor(dictionary=True)
        ret_value = function(dict_cur, *args, **kwargs)
        dict_cur.close()
        connection.close()
        return ret_value

    return wrapper
