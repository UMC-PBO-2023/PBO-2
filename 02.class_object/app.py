from flask import Flask, render_template

app = Flask(__name__)

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

class Dosen:
    def __init__(self,nidn, nama, spesialis):
        self.nidn = nidn
        self.nama = nama
        self.spesialis = spesialis
    
@app.route('/oneMahasiswa')
def oneMhs():
    mhs = Mahasiswa(220510014, 'Naha handre saputra')
    return render_template('oneMahasiswa.html', mhs=mhs)

@app.route('/manyMahasiswa')
def manyMhs():
    mhs = [
        Mahasiswa(232323, 'John'),
        Mahasiswa(222222, 'Mark'),
        Mahasiswa(343434, 'Wick'),
        Mahasiswa(444444, 'Nana'),
        Mahasiswa(232323, 'Bill'),
    ]
    return render_template('manyMahasiswa.html', mhs=mhs)

@app.route('/manyDosen')
def manyDosen():
    dosen = [
        Dosen(111, 'Agung', 'Rpl'),
        Dosen(222, 'Bobon', 'Jaringan Komputer'),
        Dosen(333, 'Candra', 'Sains Data'),
        Dosen(444, 'Deden', 'Pemrograman Mobile'),
        Dosen(555, 'Endra', 'Basis Data'),
    ]
    return render_template('manyDosen.html', dosen=dosen)



if __name__ == '__main__':
    app.run(debug=True)