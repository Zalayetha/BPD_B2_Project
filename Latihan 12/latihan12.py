#main class 
class Pegawai:
     "Representasi kelas Pegawai"
     def __init__(self,idnumber,nama,telepon,departemen):
          self.idnumber = idnumber
          self.nama = nama
          self.telepon = telepon
          self.departemen = departemen


#subclass Pegawai_Tetap
class Pegawai_Tetap(Pegawai):
     "Representasi kelas Pegawai_Tetap"
     jumlah_gaji = 0
     def __init__(self, idnumber, nama, telepon, departemen,gaji_pokok,uangmakan,uangtransport):
         super().__init__(idnumber, nama, telepon, departemen)
         self.gaji_pokok = gaji_pokok
         self.uangmakan = uangmakan
         self.uangtransport = uangtransport
         
     # Method Tampil_Gaji untuk menghitung jumlah gaji
     def tampil_gaji(self):
          Pegawai_Tetap.jumlah_gaji = self.gaji_pokok + self.uangmakan + self.uangtransport
          return Pegawai_Tetap.jumlah_gaji
     
     # Method Tampil_info untuk menampilkan identitas dari kelas Pegawai
     def tampil_info(self):
          cetak = print(f'''
===============================================
               Pegawai Tetap
===============================================
ID Number      : {self.idnumber}
Nama Pegawai   : {self.nama}
Telepon        : {self.telepon}
Departemen     : {self.departemen}
Gaji Pokok     : {self.gaji_pokok}
Uang Makan     : {self.uangmakan}
Uang Transport : {self.uangtransport}
Jumlah Gaji    : {Pegawai_Tetap.jumlah_gaji}
          ''')
          return cetak


# subclass Pegawai_Honorer
class Pegawai_Honorer(Pegawai) :
     "Representasi kelas Pegawai_Honorer"
     jumlah_incentif = 0
     def __init__(self, idnumber, nama, telepon, departemen,honor):
         super().__init__(idnumber, nama, telepon, departemen)
         self.honor = honor

     # Method Tampil_Incentif
     def tampil_incentif(self):
         Pegawai_Honorer.jumlah_incentif = self.honor
         return Pegawai_Honorer.jumlah_incentif
     
     # Method Tampil_info
     def tampil_info(self):
          cetak = print(f'''
===============================================
               Pegawai Honorer
===============================================
ID Number      : {self.idnumber}
Nama Pegawai   : {self.nama}
Telepon        : {self.telepon}
Departemen     : {self.departemen}
Honor          : {Pegawai_Honorer.jumlah_incentif}
''')
          return cetak

# Deklarasi Variabel 
pegawai1 = Pegawai_Tetap('1','Mohammad Zaghy Zalayetha Sofjan','911','Departemen Teknologi Informasi',5000000,1000000,500000)
pegawai2 = Pegawai_Honorer('2','Eren Jaeger','110','Departemen Survey Corps',3000000)

#list Pegawai
Pegawai = [pegawai1,pegawai2]

#Cetak identitas dari kelas Pegawai
for pegawai in Pegawai:
     if pegawai == pegawai1 :
          pegawai.tampil_gaji()
          pegawai.tampil_info()
     
     elif pegawai == pegawai2 :
          pegawai.tampil_incentif()
          pegawai.tampil_info()

         