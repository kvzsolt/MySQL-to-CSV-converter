import connection
import os


@connection.connection_handler
def get_database_name(cursor):
    query = """
        SHOW TABLES FROM {dbname}
        """.format(dbname=os.environ.get('MYSQL_DB_NAME'))
    cursor.execute(query)
    return cursor.fetchall()


@connection.connection_handler
def get_all_data(cursor, table):
    query = """
    SELECT * FROM {table}
    """.format(table=table)
    cursor.execute(query)
    return cursor.fetchall()
