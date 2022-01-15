import mysql.connector

dict_buku = {} # membuat tipe dictionary

kdbuku = input('Masukkan kode buku : ')

dict_buku['kode'] = kdbuku

# saya tidak mencantumkan password untuk user root dikarenakan credential dari root saya tidak memiliki password 
nama_db = {
     'user':'root','host':'localhost','database':'dbpenjualan'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
sql = ('DELETE FROM buku WHERE kode = %(kode)s')
kursor.execute(sql,dict_buku)
koneksi.commit()
print('{} data diubah'.format(kursor.rowcount))
koneksi.close()