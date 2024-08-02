# routes/khsRoute.py

from flask import *
from .KhsView import *

app_khs = Blueprint('app_khs', __name__, template_folder='templates')
app_khs.add_url_rule('/', 'index', KhsView().index, methods=['GET'])
app_khs.add_url_rule('/khs/create', 'create', KhsView().create, methods=['GET'])
app_khs.add_url_rule('/khs/edit/<int:khs_id>', 'edit', KhsView().edit, methods=['GET'])
app_khs.add_url_rule('/khs/store', 'store', KhsView().store, methods=['POST'])
app_khs.add_url_rule('/khs/update/<int:khs_id>', 'update', KhsView().update, methods=['POST'])
app_khs.add_url_rule('/khs/delete/<int:khs_id>', 'delete', KhsView().delete, methods=['GET'])
