# routes/rekapRoute.py

from flask import *
from .RekapView import *

app_rekap = Blueprint('app_rekap', __name__, template_folder='templates')
app_rekap.add_url_rule('/rekap', 'index', RekapView().index, methods=['GET'])
app_rekap.add_url_rule('/rekap/create', 'create', RekapView().create, methods=['GET'])
app_rekap.add_url_rule('/rekap/edit/<int:rekap_id>', 'edit', RekapView().edit, methods=['GET'])
app_rekap.add_url_rule('/rekap/store', 'store', RekapView().store, methods=['POST'])
app_rekap.add_url_rule('/rekap/update/<int:rekap_id>', 'update', RekapView().update, methods=['POST'])
app_rekap.add_url_rule('/rekap/delete/<int:rekap_id>', 'delete', RekapView().delete, methods=['GET'])
