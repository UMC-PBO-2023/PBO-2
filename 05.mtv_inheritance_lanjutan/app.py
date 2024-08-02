from flask import Flask, render_template
from mahasiswa.routes.Route import app_mahasiswa
from dosen.routes.DosenRoute import app_dosen

app = Flask(__name__)

app.register_blueprint(app_mahasiswa, url_prefix='/mahasiswa')
app.register_blueprint(app_dosen, url_prefix='/dosen')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()