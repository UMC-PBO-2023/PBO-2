from connection import get_db
from interfaces.DosenInterface import *

class DosenModel(DosenInterface):
    @staticmethod
    def all():
        connection = get_db()
        cursor = connection.cursor()

        query = 'SELECT * FROM dosen'
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()

        return results
    
    @staticmethod
    def find(dosen_id):
        connection = get_db()
        cursor = connection.cursor()

        query = 'SELECT * FROM dosen WHERE id = %s LIMIT 1'
        cursor.execute(query, (dosen_id))
        result = cursor.fetchone()

        cursor.close()

        return result
    
    @staticmethod
    def store(dosen_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = 'INSERT INTO dosen (nidn, nama, bidang) VALUES (%s, %s, %s)'
        cursor.execute(query, (dosen_obj.nidn, dosen_obj.nama, dosen_obj.bidang))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(dosen_id, dosen_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = 'UPDATE dosen SET nidn = %s, nama = %s, bidang = %s WHERE id = %s'
        cursor.execute(query, (dosen_obj.nidn, dosen_obj.nama, dosen_obj.bidang, dosen_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(dosen_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "DELETE FROM dosen WHERE id = %s"
        cursor.execute(query, (dosen_id))

        connection.commit()
        cursor.close()
        connection.close()


