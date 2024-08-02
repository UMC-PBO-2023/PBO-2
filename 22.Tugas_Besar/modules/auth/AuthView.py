from flask import *
from .AuthModel import *
import base64

class AuthView():

    @staticmethod
    def index():
        data = AuthModel().all()
        return render_template('login.html', data=json.dumps(data))
    
    @staticmethod
    def create():
        return render_template('register.html')
    
    @staticmethod
    def store():
        auth_obj=AuthModel()
        post = request.form

        auth_obj.nama = post['nama']
        auth_obj.username = post['username']
        auth_obj.password= post['password']
        auth_obj.photo=  post['photo']

        AuthModel().store(auth_obj)
        return redirect('/auth/login')
    
    @staticmethod
    def edit(auth_id):
        obj = AuthModel().find(auth_id)
        return render_template('user_edit.html', obj=obj)
    
    @staticmethod
    def update(auth_id):
        data = AuthModel().find(auth_id)
        if data :
            post = request.form
            auth_obj = AuthModel()
            auth_obj.nama = post['nama']
            auth_obj.username = post['username']
            auth_obj.password= post['password']
            auth_obj.photo=  post['photo']
            AuthModel().update(auth_id, auth_obj)
            return redirect('/')
        else :
            return redirect(request.referrer)
    
    @staticmethod
    def delete(auth_id):
        data = AuthModel().find(auth_id)
        if data :
            AuthModel().delete(auth_id)
            return redirect('/auth/login')
        else:
            return redirect(request.referrer)