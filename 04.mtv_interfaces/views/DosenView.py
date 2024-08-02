from flask import *
from models.DosenModel import *

class DosenView:
    @staticmethod
    def index():
        data = DosenModel().all()
        return render_template('dosen_index.html', data=data)

    @staticmethod
    def create():
        return render_template('dosen_create.html')
    
    @staticmethod
    def store():
        post = request.form
        dosen_obj = DosenModel()
        dosen_obj.nidn = post['nidn']
        dosen_obj.nama = post['nama']
        dosen_obj.bidang = post['bidang']
        DosenModel.store(dosen_obj)

        return redirect('/dosen')
    
    @staticmethod
    def edit(dosen_id):
        obj = DosenModel.find(dosen_id)
        return render_template('dosen_update.html', obj=obj)
    
    @staticmethod
    def update(dosen_id):
       data = DosenModel.find(dosen_id)

       if data:
        post = request.form
        dosen_obj = DosenModel()
        dosen_obj.nidn = post['nidn']
        dosen_obj.nama = post['nama']
        dosen_obj.bidang = post['bidang']
        DosenModel.update(dosen_id, dosen_obj)
        
        return redirect('/dosen')
       
       else:
          return redirect(request.referrer)

    @staticmethod
    def delete(dosen_id):
       data = DosenModel.find(dosen_id)

       if data:
          DosenModel.delete(dosen_id)
          return redirect('/dosen')
       
       else:
          return redirect(request.referrer)

