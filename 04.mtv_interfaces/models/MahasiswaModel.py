from connection import get_db
from interfaces.MahasiswaInterface import *

class MahasiswaModel(MahasiswaInterface):
    @staticmethod
    def all():
        connection = get_db()
        cursor = connection.cursor()

        query = 'SELECT * FROM mahasiswa_pbo2'
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()

        return results
    
    @staticmethod
    def find(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = 'SELECT * FROM mahasiswa_pbo2 WHERE id = %s LIMIT 1'
        cursor.execute(query, (mahasiswa_id))
        result = cursor.fetchone()

        cursor.close()

        return result
    
    @staticmethod
    def store(mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = 'INSERT INTO mahasiswa_pbo2 (nim, nama, kelas, program_studi, fakultas) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.kelas, mahasiswa_obj.program_studi, mahasiswa_obj.fakultas))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def update(mahasiswa_id, mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = 'UPDATE  mahasiswa_pbo2 SET nim = %s, nama = %s, kelas = %s, program_studi = %s, fakultas = %s WHERE id = %s'
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.kelas, mahasiswa_obj.program_studi, mahasiswa_obj.fakultas, mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "DELETE FROM  mahasiswa_pbo2 WHERE id = %s"
        cursor.execute(query, (mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()


