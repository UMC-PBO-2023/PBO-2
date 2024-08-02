# routes/khsRoute.py

from flask import *
from .AuthView import *

app_auth = Blueprint('app_auth', __name__, template_folder='templates')
app_auth.add_url_rule('/auth/login', 'index', AuthView().index, methods=['GET'])
app_auth.add_url_rule('/auth/register', 'create', AuthView().create, methods=['GET'])
app_auth.add_url_rule('/auth/edit/<int:auth_id>', 'edit', AuthView().edit, methods=['GET'])
app_auth.add_url_rule('/auth/store', 'store', AuthView().store, methods=['POST'])
app_auth.add_url_rule('/auth/update/<int:auth_id>', 'update', AuthView().update, methods=['POST'])
app_auth.add_url_rule('/auth/delete/<int:auth_id>', 'delete', AuthView().delete, methods=['GET'])

