# models/DosenModels.py
from core.CoreModel import CoreModel

class RekapModel(CoreModel):

    def __init__(self):
        self.table_name = "rekap_biaya"
        self.table_id = "id"