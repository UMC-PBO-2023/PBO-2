import pymysql

def get_db():
    connection = pymysql.connect(
        host='localhost', 
        user='root', 
        password='root', 
        database='dbumc_pbo', 
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection