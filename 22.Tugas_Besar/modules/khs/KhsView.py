from flask import *
from .KhsModel import *

class KhsView():

    @staticmethod
    def index():
        data = KhsModel().all()
        return render_template('khs_index.html', data=data, json=json.dumps(data))
    
    @staticmethod
    def create():
        return render_template('khs_create.html')
    
    @staticmethod
    def store():
        khs_obj=KhsModel()
        post = request.form
        khs_obj.nim = post['nim']
        khs_obj.nama_mhs = post['nama_mhs']
        khs_obj.kelas = post['kelas']
        khs_obj.prodi = post['prodi']
        khs_obj.homebase = post['homebase']
        khs_obj.sks_basis_data = post['sks_basis_data']
        khs_obj.nilai_basis_data = post['nilai_basis_data']
        khs_obj.bobot_basis_data = post['bobot_basis_data']
        khs_obj.am_basis_data = post['am_basis_data']
        khs_obj.sks_etika_profesi = post['sks_etika_profesi']
        khs_obj.nilai_etika_profesi = post['nilai_etika_profesi']
        khs_obj.bobot_etika_profesi = post['bobot_etika_profesi']
        khs_obj.am_etika_profesi = post['am_etika_profesi']
        khs_obj.sks_pbo2 = post['sks_pbo2']
        khs_obj.nilai_pbo2 = post['nilai_pbo2']
        khs_obj.bobot_pbo2 = post['bobot_pbo2']
        khs_obj.am_pbo2 = post['am_pbo2']
        khs_obj.sks_jaringan_komputer = post['sks_jaringan_komputer']
        khs_obj.nilai_jaringan_komputer = post['nilai_jaringan_komputer']
        khs_obj.bobot_jaringan_komputer = post['bobot_jaringan_komputer']
        khs_obj.am_jaringan_komputer = post['am_jaringan_komputer']
        khs_obj.sks_robotika = post['sks_robotika']
        khs_obj.nilai_robotika = post['nilai_robotika']
        khs_obj.bobot_robotika = post['bobot_robotika']
        khs_obj.am_robotika = post['am_robotika']
        KhsModel().store(khs_obj)
        return redirect('/')
    
    @staticmethod
    def edit(khs_id):
        obj = KhsModel().find(khs_id)
        return render_template('khs_edit.html', obj=obj)
    
    @staticmethod
    def update(khs_id):
        data = KhsModel().find(khs_id)
        if data :
            post = request.form
            print(post)
            khs_obj = KhsModel()
            khs_obj.nim = post['nim']
            khs_obj.nama_mhs = post['nama_mhs']
            khs_obj.kelas = post['kelas']
            khs_obj.prodi = post['prodi']
            khs_obj.homebase = post['homebase']
            khs_obj.sks_basis_data = post['sks_basis_data']
            khs_obj.nilai_basis_data = post['nilai_basis_data']
            khs_obj.bobot_basis_data = post['bobot_basis_data']
            khs_obj.am_basis_data = post['am_basis_data']
            khs_obj.sks_etika_profesi = post['sks_etika_profesi']
            khs_obj.nilai_etika_profesi = post['nilai_etika_profesi']
            khs_obj.bobot_etika_profesi = post['bobot_etika_profesi']
            khs_obj.am_etika_profesi = post['am_etika_profesi']
            khs_obj.sks_pbo2 = post['sks_pbo2']
            khs_obj.nilai_pbo2 = post['nilai_pbo2']
            khs_obj.bobot_pbo2 = post['bobot_pbo2']
            khs_obj.am_pbo2 = post['am_pbo2']
            khs_obj.sks_jaringan_komputer = post['sks_jaringan_komputer']
            khs_obj.nilai_jaringan_komputer = post['nilai_jaringan_komputer']
            khs_obj.bobot_jaringan_komputer = post['bobot_jaringan_komputer']
            khs_obj.am_jaringan_komputer = post['am_jaringan_komputer']
            khs_obj.sks_robotika = post['sks_robotika']
            khs_obj.nilai_robotika = post['nilai_robotika']
            khs_obj.bobot_robotika = post['bobot_robotika']
            khs_obj.am_robotika = post['am_robotika']
            KhsModel().update(khs_id, khs_obj)
            return redirect('/')
        else :
            return redirect(request.referrer)
    
    @staticmethod
    def delete(khs_id):
        data = KhsModel().find(khs_id)
        if data :
            KhsModel().delete(khs_id)
            return redirect('/')
        else:
            return redirect(request.referrer)