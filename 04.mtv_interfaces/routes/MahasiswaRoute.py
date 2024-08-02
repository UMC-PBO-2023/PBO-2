from flask import *
from views.MahasiswaView import *

app_mahasiswa = Blueprint('app_mahasiswa', __name__, template_folder='templates')

app_mahasiswa.add_url_rule('/', 'index', MahasiswaView().index, methods=['GET'])

app_mahasiswa.add_url_rule('/create-mahasiswa', 'create-mahasiswa', MahasiswaView().create, methods=['GET'])

app_mahasiswa.add_url_rule('/edit-mahasiswa/<int:mahasiswa_id>', 'edit-mahasiswa', MahasiswaView().edit, methods=['GET'])

app_mahasiswa.add_url_rule('/store-mahasiswa', 'store-mahasiswa', MahasiswaView().store, methods=['POST'])

app_mahasiswa.add_url_rule('/update-mahasiswa/<int:mahasiswa_id>', 'update-mahasiswa', MahasiswaView().update, methods=['POST'])

app_mahasiswa.add_url_rule('/delete-mahasiswa/<int:mahasiswa_id>', 'delete-mahasiswa', MahasiswaView().delete, methods=['GET'])
