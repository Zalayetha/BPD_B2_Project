import mysql.connector

mydict = {}

# input data
nim = input('Masukkan NIM anda : ')


# memasukan nilai 
mydict['NIM'] = nim

db_name = mysql.connector.connect(user='root',host='localhost',database='dbpenjualan')
mycursor = db_name.cursor()

# sintaks sql
sql =('DELETE FROM mahasiswa WHERE NIM = %(NIM)s')

# execute
mycursor.execute(sql,mydict)
db_name.commit()
print('{} data dihapus'.format(mycursor.rowcount))

# close connection
mycursor.close()     
db_name.close()