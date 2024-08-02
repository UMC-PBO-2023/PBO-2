from connection import get_db
from dosen.coremodels.CoreModelDosen import CoreModelDosen

class DosenModel(CoreModelDosen):
    def __init__(self):
        self.table_name = "dosen"
        self.table_id = "id"