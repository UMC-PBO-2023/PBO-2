from flask import *
from .LokerModel import *

class LokerView():

    @staticmethod
    def index():
        data = LokerModel().all()
        return render_template('loker_index.html', data=data)
    
    @staticmethod
    def detail(loker_id):
        obj = LokerModel().find(loker_id)
        return render_template('loker_detail.html', obj=obj)
    
    @staticmethod
    def create():
        return render_template('loker_create.html')
    
    @staticmethod
    def store():
        loker_obj=LokerModel()
        post = request.form
        loker_obj.perusahaan = post['perusahaan']
        loker_obj.posisi = post['posisi']
        loker_obj.category = post['category']
        loker_obj.alamat = post['alamat']
        loker_obj.keterangan = post['keterangan']
        loker_obj.photo = post['photo']

  
        LokerModel().store(loker_obj)
        return redirect('/loker')
    
    @staticmethod
    def edit(loker_id):
        obj = LokerModel().find(loker_id)
        return render_template('loker_edit.html', obj=obj)
    
    @staticmethod
    def update(loker_id):
        data = LokerModel().find(loker_id)
        if data :
            post = request.form
            print(post)
            loker_obj = LokerModel()
            loker_obj.perusahaan = post['perusahaan']
            loker_obj.posisi = post['posisi']
            loker_obj.category = post['category']
            loker_obj.alamat = post['alamat']
            loker_obj.keterangan = post['keterangan']
            loker_obj.photo = post['photo']
     
            
            LokerModel().update(loker_id, loker_obj)
            return redirect('/loker')
        else :
            return redirect(request.referrer)
    
    @staticmethod
    def delete(loker_id):
        data = LokerModel().find(loker_id)
        if data :
            LokerModel().delete(loker_id)
            return redirect('/loker')
        else:
            return redirect(request.referrer)