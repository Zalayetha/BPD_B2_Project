import datetime as dt
tahun_ini = dt.datetime.today()
ulang = 1

while(ulang == 1):
     nama_karyawan = input('Masukkan nama anda :')
     NIP = input('Masukkan NIP anda :')
     input_tahun_masuk = input('Masukkan tahun masuk anda :')

     #proses perhitungan lama kerja
     tahun_masuk = dt.datetime.strptime(input_tahun_masuk,"%Y")
     lama_kerja = (tahun_ini - tahun_masuk).days //365
     print(f'Anda kerja selama {lama_kerja} tahun' )

     jabatan = input('Masukkan jabatan anda (cth : staff,manager,direktur) :')
     status_karyawan = input('Masukkan status karyawan anda (cth : tetap,honorer) :')
     status_pernikahan = input('Masukkan status pernikahan anda (cth: menikah / belum menikah) :')


     #proses gapok 
     if jabatan in ('direktur') :
          gapok = 7000000
     elif jabatan in ('manager'):
          gapok = 3500000
     elif jabatan in ('staff') :
          gapok = 1500000
     else :
          gapok = 1000000

     #proses tunjangan status karyawan
     if status_karyawan in ('tetap') :
          tunjangan_transport = 0
          tunjangan_tetap = 2 * gapok + tunjangan_transport   
     elif status_karyawan in ('honorer') :
          tunjangan_transport = 25 * 150000
          tunjangan_tetap = 0

     #proses tunjangan status
     if status_pernikahan in ('menikah') :
          tunjangan_istri = 250000
          jumlah_anak = int(input('Masukan jumlah anak anda : '))
          if jumlah_anak <= 3 :
               tunjangan_anak = 200000 * jumlah_anak
          else :
               tunjangan_anak = 200000 * 3
     
     else :
          tunjangan_istri = 0
          tunjangan_anak = 0

     #proses total gaji
     total_gaji = gapok + tunjangan_tetap + tunjangan_transport + tunjangan_istri +tunjangan_anak
     PPH = 0.05 * gapok
     gaji_bersih = total_gaji - PPH

     #output
     print(f'''
     ===================================================
     Nama Pegawai             : {nama_karyawan}
     NIP                      : {NIP}
     Tahun Masuk              : {input_tahun_masuk}
     Lama Kerja               : {lama_kerja} tahun

     Pilih Jabatan            :
          1. Staff
          2. Manager
          3. Direktur
     Jabatan                  : {jabatan}
     Pilih Status karyawan    :
          1. Tetap
          2. Honorer
     Status Karyawan          : {status_karyawan}
     ''')
     print(f'''
      Pilih Status pernikahan :
          1. Menikah
          2. Belum Menikah
     Status Pernikahan        : {status_pernikahan}
     ''')

     if status_pernikahan in ('menikah') :
          print(f'''
          Jumlah Anak         : {jumlah_anak}
          ''')
     
     print(f'''
     Proses Gaji Karyawan     : {nama_karyawan}
     ''')

     proses_gaji = input(f'''
     apakah anda ingin memproses (Y/T) ?
     ''')

     if proses_gaji in ('Y') :
          print(f'''
     ================================================
     Gaji Pokok          : {gapok}
          ''')
          if status_karyawan in ('tetap') :
               print(f'''
     Tunjangan Tetap     : {tunjangan_tetap}
               ''')
          elif status_karyawan in ('honorer') :
               print(f'''
     Tunjangan Transport : {tunjangan_transport}
               ''')
          if status_pernikahan in ('menikah') :
               print(f'''
     Tunjangan Istri     : {tunjangan_istri}
     Tunjangan Anak      : {tunjangan_anak}
     ================================================
               ''')
          print(f'''
     Total Gaji          : {total_gaji}
     PPH                 : {PPH}
     Gaji Bersih         : {gaji_bersih}
     ================================================
     Progammer:
          ''')
          NIM = input(f'''
          Masukan NIM programmer   :
          ''')
          if NIM in ('2111500795') :
               print(f'''
     NIM                 :21115000795
     NAMA                :M Zaghy
               ''')   
     #change condition
     pengulangan = input(f'''
     Apakah anda ingin mengulang (Y/T) ?
     ''')
     if pengulangan in ('Y') :
          ulang = 1
     else : 
          ulang = 2
