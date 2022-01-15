import mysql.connector


mydict = {}

# input data
nip = input('Masukkan NIP anda : ')
nama = input('Masukkan nama anda  : ')
jabatan = input('Masukan jabatan anda : ')
divisi = input('Masukan divisi anda : ')
gaji = int(input('Masukan gaji anda : '))

# memasukan nilai 
mydict['NIP'] = nip
mydict['NAMA'] = nama
mydict['JABATAN'] = jabatan
mydict['DIVISI'] = divisi
mydict['GAJI'] = gaji


db_name = mysql.connector.connect(user='root',host='localhost',database='dbpenjualan')
mycursor = db_name.cursor()

# sintaks sql
sql =('INSERT INTO pegawai (NIP,NAMA,JABATAN,DIVISI,GAJI) VALUES (%(NIP)s,%(NAMA)s,%(JABATAN)s,%(DIVISI)s,%(GAJI)s)')

# execute
mycursor.execute(sql,mydict)
db_name.commit()
print('{} data diubah'.format(mycursor.rowcount))

# close connection
mycursor.close()     
db_name.close()