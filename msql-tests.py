import pymysql
from pymysql import *
from auth_info import *

user_name = 'GSP_main'

user_data = auth_info[user_name]

def send_commit(sql_req, connect, curs, args=[]):
    curs.execute(f''' {sql_req} ''', args)
    connect.commit()


try:
    

    connection = connect(
        host = user_data['host'],
        user = user_name,
        password = user_data['password'],
        database = user_data['db_name'],
        charset='utf8mb4',
        cursorclass = cursors.DictCursor
        )

    print('connection established')


    try:
        cursor = connection.cursor()

        #send_commit('''INSERT INTO vio_test VALUES('Batman', 'Gotham')''', connection, cursor)
        send_commit('''SELECT * FROM vio_test''', connection, cursor)

        print(cursor.fetchall())
        
    finally:
        connection.close()

except Error as e:
    print(e)

