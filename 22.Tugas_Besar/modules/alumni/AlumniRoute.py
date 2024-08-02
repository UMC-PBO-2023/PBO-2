# routes/alumniRoute.py

from flask import *
from .AlumniView import *

app_alumni = Blueprint('app_alumni', __name__, template_folder='templates')
app_alumni.add_url_rule('/alumni', 'index', AlumniView().index, methods=['GET'])
app_alumni.add_url_rule('/alumni/create', 'create', AlumniView().create, methods=['GET'])
app_alumni.add_url_rule('/alumni/edit/<int:alumni_id>', 'edit', AlumniView().edit, methods=['GET'])
app_alumni.add_url_rule('/alumni/store', 'store', AlumniView().store, methods=['POST'])
app_alumni.add_url_rule('/alumni/update/<int:alumni_id>', 'update', AlumniView().update, methods=['POST'])
app_alumni.add_url_rule('/alumni/delete/<int:alumni_id>', 'delete', AlumniView().delete, methods=['GET'])
