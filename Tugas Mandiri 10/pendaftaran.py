import biaya
import jurusan
import kelas
global nim,nama,noHp,email,alamat,nem
def CetakHasil():
     print(f'''
======================================
          DATA MAHASISWA
======================================
NIM            : {nim}
Nama           : {nama}
Nomor HP       : {noHp}
Email          : {email}
Alamat         : {alamat}
NEM            : {nem}
''')
     jurusan.get_jurusan(nim)
     kelas.get_kelas(nim)
     biaya.get_biaya(nim)

nim = input('Masukan NIM anda : ')
nama = input('Masukan Nama Lengkap anda : ')
noHp = input('Masukan Nomor Handphone anda : ')
email = input('Masukan Email  anda : ')
alamat = input('Masukan Alamat anda : ')
nem = input('Masukan NEM anda : ')

CetakHasil()