# models/DosenModels.py
from core.CoreModel import CoreModel

class MahasiswaModel(CoreModel):

    def __init__(self):
        self.table_name = "mahasiswa_pbo2"
        self.table_id = "id"