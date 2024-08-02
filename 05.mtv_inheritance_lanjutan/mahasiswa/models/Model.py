from connection import get_db
from mahasiswa.coremodels.CoreModelMahasiswa import CoreModelMahasiswa

class MahasiswaModel(CoreModelMahasiswa):
    def __init__(self):
        self.table_name = "mahasiswa_pbo2"
        self.table_id = "id"