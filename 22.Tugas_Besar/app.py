#app.py
from flask import *
from modules.khs.KhsRoute import app_khs
from modules.auth.AuthRoute import app_auth
from modules.rekap.RekapRoute import app_rekap
from modules.loker.LokerRoute import app_loker
from modules.alumni.AlumniRoute import app_alumni

app = Flask(__name__)

app.register_blueprint(app_khs, url_prefix='/')
app.register_blueprint(app_auth, url_prefix='/')
app.register_blueprint(app_rekap, url_prefix='/')
app.register_blueprint(app_loker, url_prefix='/')
app.register_blueprint(app_alumni, url_prefix='/')


if __name__ == '__main__':
    app.run(debug=True)