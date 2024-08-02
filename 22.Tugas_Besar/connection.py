import pymysql

def get_db():
    connection = pymysql.connect(
        host='localhost', 
        user='root', 
        password='root', 
        database='pbo2_tgs_besar', 
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection