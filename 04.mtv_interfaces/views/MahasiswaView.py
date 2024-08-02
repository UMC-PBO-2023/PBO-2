from flask import *
from models.MahasiswaModel import *

class MahasiswaView:
    @staticmethod
    def index():
        data = MahasiswaModel().all()
        return render_template('mahasiswa_index.html', data=data)

    @staticmethod
    def create():
        return render_template('mahasiswa_create.html')
    
    @staticmethod
    def store():
        post = request.form
        mahasiswa_obj = MahasiswaModel()
        mahasiswa_obj.nim = post['nim']
        mahasiswa_obj.nama = post['nama']
        mahasiswa_obj.kelas = post['kelas']
        mahasiswa_obj.program_studi = post['program_studi']
        mahasiswa_obj.fakultas = post['fakultas']
        MahasiswaModel.store(mahasiswa_obj)

        return redirect('/mahasiswa')
    
    @staticmethod
    def edit(mahasiswa_id):
        obj = MahasiswaModel.find(mahasiswa_id)
        return render_template('mahasiswa_update.html', obj=obj)
    
    @staticmethod
    def update(mahasiswa_id):
       data = MahasiswaModel.find(mahasiswa_id)

       if data:
        post = request.form
        mahasiswa_obj = MahasiswaModel()
        mahasiswa_obj.nim = post['nim']
        mahasiswa_obj.nama = post['nama']
        mahasiswa_obj.kelas = post['kelas']
        mahasiswa_obj.program_studi = post['program_studi']
        mahasiswa_obj.fakultas = post['fakultas']
        MahasiswaModel.update(mahasiswa_id, mahasiswa_obj)
        
        return redirect('/mahasiswa')
       
       else:
          return redirect(request.referrer)

    @staticmethod
    def delete(mahasiswa_id):
       data = MahasiswaModel.find(mahasiswa_id)

       if data:
          MahasiswaModel.delete(mahasiswa_id)
          return redirect('/mahasiswa')
       
       else:
          return redirect(request.referrer)

