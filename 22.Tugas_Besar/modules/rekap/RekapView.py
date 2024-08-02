from flask import *
from .RekapModel import *

class RekapView():

    @staticmethod
    def index():
        data = RekapModel().all()
        return render_template('rekap_index.html', data=data, json=json.dumps(data))
    
    @staticmethod
    def create():
        return render_template('rekap_create.html')
    
    @staticmethod
    def store():
        rekap_obj=RekapModel()
        post = request.form
        rekap_obj.nim = post['nim']
        rekap_obj.nama_mhs = post['nama_mhs']
        rekap_obj.kelas = post['kelas']
        rekap_obj.prodi = post['prodi']
        rekap_obj.fakultas = post['fakultas']
        rekap_obj.ukt_smt1 = post['ukt_smt1']
        rekap_obj.ukt_smt2 = post['ukt_smt2']
        rekap_obj.ukt_smt3 = post['ukt_smt3']
        rekap_obj.ukt_smt4 = post['ukt_smt4']
        rekap_obj.ukt_smt5 = post['ukt_smt5']
        rekap_obj.ukt_smt6 = post['ukt_smt6']
        rekap_obj.uang_gedung = post['uang_gedung']
        rekap_obj.dpp = post['dpp']
        rekap_obj.total = int(post['ukt_smt1']) + int(post['ukt_smt2']) +int(post['ukt_smt3']) +int(post['ukt_smt4']) +int(post['ukt_smt5']) +int(post['ukt_smt6']) +int(post['uang_gedung']) +int(post['dpp'])
  
        RekapModel().store(rekap_obj)
        return redirect('/rekap')
    
    @staticmethod
    def edit(rekap_id):
        obj = RekapModel().find(rekap_id)
        return render_template('rekap_edit.html', obj=obj)
    
    @staticmethod
    def update(rekap_id):
        data = RekapModel().find(rekap_id)
        if data :
            post = request.form
            print(post)
            rekap_obj = RekapModel()
            rekap_obj.nim = post['nim']
            rekap_obj.nama_mhs = post['nama_mhs']
            rekap_obj.kelas = post['kelas']
            rekap_obj.prodi = post['prodi']
            rekap_obj.fakultas = post['fakultas']
            rekap_obj.ukt_smt1 = post['ukt_smt1']
            rekap_obj.ukt_smt2 = post['ukt_smt2']
            rekap_obj.ukt_smt3 = post['ukt_smt3']
            rekap_obj.ukt_smt4 = post['ukt_smt4']
            rekap_obj.ukt_smt5 = post['ukt_smt5']
            rekap_obj.ukt_smt6 = post['ukt_smt6']
    
            rekap_obj.uang_gedung = post['uang_gedung']
            rekap_obj.dpp = post['dpp']
            rekap_obj.total = int(post['ukt_smt1']) + int(post['ukt_smt2']) +int(post['ukt_smt3']) +int(post['ukt_smt4']) +int(post['ukt_smt5']) +int(post['ukt_smt6']) +int(post['uang_gedung']) +int(post['dpp'])
            
            RekapModel().update(rekap_id, rekap_obj)
            return redirect('/rekap')
        else :
            return redirect(request.referrer)
    
    @staticmethod
    def delete(rekap_id):
        data = RekapModel().find(rekap_id)
        if data :
            RekapModel().delete(rekap_id)
            return redirect('/rekap')
        else:
            return redirect(request.referrer)