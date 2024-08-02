from flask import render_template, request, redirect
from dosen.models.DosenModel import DosenModel

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
        dosen_obj = DosenModel()
        post = request.form
        dosen_obj.nidn = post['nidn']
        dosen_obj.nama = post['nama']
        dosen_obj.bidang = post['bidang']
        DosenModel().store(dosen_obj)
        return redirect('/dosen')

    @staticmethod
    def edit(dosen_id):
        obj = DosenModel().find(dosen_id)
        if obj:
            return render_template('dosen_edit.html', obj=obj)
        else:
            return "Dosen not found", 404
    
    @staticmethod
    def update(dosen_id):
        data = DosenModel().find(dosen_id)
        if data:
            post = request.form
            dosen_obj = DosenModel()
            dosen_obj.nidn = post['nidn']
            dosen_obj.nama = post['nama']
            dosen_obj.bidang = post['bidang']
            DosenModel().update(dosen_id, dosen_obj)
            return redirect('/dosen')
        else:
            return "Dosen not found", 404
        
    @staticmethod
    def delete(dosen_id):
        data = DosenModel().find(dosen_id)
        if data:
            DosenModel().delete(dosen_id)
            return redirect('/dosen')
        else:
            return "Dosen not found", 404
