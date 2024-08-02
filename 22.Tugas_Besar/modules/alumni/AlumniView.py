from flask import *
from .AlumniModel import *

class AlumniView():

    @staticmethod
    def index():
        data = AlumniModel().all()
        return render_template('alumni_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('alumni_create.html')
    
    @staticmethod
    def store():
        alumni_obj=AlumniModel()
        post = request.form
        alumni_obj.nama = post['nama']
        alumni_obj.tgl_yudisium = post['tgl_yudisium']
        alumni_obj.judul_skripsi = post['judul_skripsi']
        alumni_obj.ipk_lulus = post['ipk_lulus']
        alumni_obj.perusahaan = post['perusahaan']
        alumni_obj.posisi = post['posisi']

  
        AlumniModel().store(alumni_obj)
        return redirect('/alumni')
    
    @staticmethod
    def edit(alumni_id):
        obj = AlumniModel().find(alumni_id)
        return render_template('alumni_edit.html', obj=obj)
    
    @staticmethod
    def update(alumni_id):
        data = AlumniModel().find(alumni_id)
        if data :
            post = request.form
            print(post)
            alumni_obj = AlumniModel()
            alumni_obj.nama = post['nama']
            alumni_obj.tgl_yudisium = post['tgl_yudisium']
            alumni_obj.judul_skripsi = post['judul_skripsi']
            alumni_obj.ipk_lulus = post['ipk_lulus']
            alumni_obj.perusahaan = post['perusahaan']
            alumni_obj.posisi = post['posisi']

            
            
            AlumniModel().update(alumni_id, alumni_obj)
            return redirect('/alumni')
        else :
            return redirect(request.referrer)
    
    @staticmethod
    def delete(alumni_id):
        data = AlumniModel().find(alumni_id)
        if data :
            AlumniModel().delete(alumni_id)
            return redirect('/alumni')
        else:
            return redirect(request.referrer)