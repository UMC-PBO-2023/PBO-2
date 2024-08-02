# routes/DosenRoute.py

from flask import *
from .DosenView import *

app_dosen = Blueprint('app_dosen', __name__, template_folder='templates')
app_dosen.add_url_rule('/', 'index', DosenView().index, methods=['GET'])
app_dosen.add_url_rule('/dosen/create', 'create', DosenView().create, methods=['GET'])
app_dosen.add_url_rule('/dosen/edit/<int:dosen_id>', 'edit', DosenView().edit, methods=['GET'])
app_dosen.add_url_rule('/dosen/store', 'store', DosenView().store, methods=['POST'])
app_dosen.add_url_rule('/dosen/update/<int:dosen_id>', 'update', DosenView().update, methods=['POST'])
app_dosen.add_url_rule('/dosen/delete/<int:dosen_id>', 'delete', DosenView().delete, methods=['GET'])
