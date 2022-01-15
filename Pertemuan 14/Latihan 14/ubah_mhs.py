import mysql.connector

mydict = {}

# input data
nim = input('Masukkan NIM anda : ')
nama = input('Masukkan nama anda  : ')
alamat = input('Masukan alamat anda : ')
telepon = input('Masukan nomor telepon anda : ')
jurusan = input('Masukan jurusan anda : ')

# memasukan nilai 
mydict['NIM'] = nim
mydict['NAMA'] = nama
mydict['ALAMAT'] = alamat
mydict['TELEPON'] = telepon
mydict['JURUSAN'] = jurusan


db_name = mysql.connector.connect(user='root',host='localhost',database='dbpenjualan')
mycursor = db_name.cursor()

# sintaks sql
sql =('UPDATE mahasiswa SET NIM = %(NIM)s,NAMA = %(NAMA)s,ALAMAT = %(ALAMAT)s,TELEPON = %(TELEPON)s,JURUSAN = %(JURUSAN)s WHERE NIM = %(NIM)s')

# execute
mycursor.execute(sql,mydict)
db_name.commit()
print('{} data diubah'.format(mycursor.rowcount))

# close connection
mycursor.close()     
db_name.close()