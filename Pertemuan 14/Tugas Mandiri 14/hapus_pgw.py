import mysql.connector

mydict = {}

# input data
nip = input('Masukkan NIP anda : ')


# memasukan nilai 
mydict['NIP'] = nip

db_name = mysql.connector.connect(user='root',host='localhost',database='dbpenjualan')
mycursor = db_name.cursor()

# sintaks sql
sql =('DELETE FROM pegawai WHERE NIP = %(NIP)s')

# execute
mycursor.execute(sql,mydict)
db_name.commit()
print('{} data dihapus'.format(mycursor.rowcount))

# close connection
mycursor.close()     
db_name.close()