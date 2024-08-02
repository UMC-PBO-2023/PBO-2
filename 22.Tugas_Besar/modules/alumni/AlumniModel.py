# models/DosenModels.py
from core.CoreModel import CoreModel

class AlumniModel(CoreModel):

    def __init__(self):
        self.table_name = "alumni"
        self.table_id = "id"