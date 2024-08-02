# routes/lokerRoute.py

from flask import *
from .LokerView import *

app_loker = Blueprint('app_loker', __name__, template_folder='templates')
app_loker.add_url_rule('/loker', 'index', LokerView().index, methods=['GET'])
app_loker.add_url_rule('/loker/create', 'create', LokerView().create, methods=['GET'])
app_loker.add_url_rule('/loker/edit/<int:loker_id>', 'edit', LokerView().edit, methods=['GET'])
app_loker.add_url_rule('/loker/detail/<int:loker_id>', 'detail', LokerView().detail, methods=['GET'])
app_loker.add_url_rule('/loker/store', 'store', LokerView().store, methods=['POST'])
app_loker.add_url_rule('/loker/update/<int:loker_id>', 'update', LokerView().update, methods=['POST'])
app_loker.add_url_rule('/loker/delete/<int:loker_id>', 'delete', LokerView().delete, methods=['GET'])
