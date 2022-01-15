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
sql =('UPDATE pegawai SET NIP = %(NIP)s,NAMA = %(NAMA)s,JABATAN = %(JABATAN)s,DIVISI = %(DIVISI)s,GAJI = %(GAJI)s WHERE NIP = %(NIP)s')

# execute
mycursor.execute(sql,mydict)
db_name.commit()
print('{} data diubah'.format(mycursor.rowcount))

# close connection
mycursor.close()     
db_name.close()