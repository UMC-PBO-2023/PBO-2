from flask import *
from routes.DosenRoute import app_dosen
from routes.MahasiswaRoute import app_mahasiswa

app = Flask(__name__)

app.register_blueprint(app_dosen, url_prefix='/dosen')
app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')

@app.route('/')
def template():
    return render_template('beranda.html')




if __name__ == '__main__':
    app.run(debug=True)