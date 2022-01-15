import mysql.connector

dict_buku = {} # membuat tipe dictionary

kdbuku = input('Masukkan kode buku : ')
judul = input('Masukkan judul buku : ')
harga = int(input('Masukkan harga buku : '))
penerbit = input('Masukkan penerbit : ')
tahun = int(input('Masukkan tahun buku : '))

dict_buku['kode'] = kdbuku
dict_buku['judul'] = judul
dict_buku['harga'] = harga
dict_buku['penerbit'] = penerbit
dict_buku['tahun'] = tahun

# saya tidak mencantumkan password untuk user root dikarenakan credential dari root saya tidak memiliki password 
nama_db = {
     'user':'root','host':'localhost','database':'dbpenjualan'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
sql = ('UPDATE buku SET judul = %(judul)s, harga = %(harga)s,penerbit = %(penerbit)s, tahun = %(tahun)s WHERE kode = %(kode)s')
koneksi.commit()
print('{} data diubah'.format(kursor.rowcount))
koneksi.close()