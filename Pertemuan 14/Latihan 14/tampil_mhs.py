import mysql.connector

def main():
     try:
          db_name = {'user':'root','host':'localhost','database':'dbpenjualan'}
          myconnect = mysql.connector.connect(**db_name)
          mycursor = myconnect.cursor()     
          sql = ('SELECT * FROM mahasiswa ORDER BY nim')

          # execute 
          mycursor.execute(sql)
          
          # result menggunakan fetchall
          result = mycursor.fetchall()
          print(f'{mycursor.rowcount} data yang diambil')

          for row in result :
               nim = row[0]
               nama = row[1]
               alamat = row[2]
               telepon = row[3]
               jurusan = row[4]

               print(f'''
NIM       : {nim}
Nama      : {nama}
Alamat    : {alamat}
Telepon   : {telepon}
Jurusan   : {jurusan}
               ''')
          mycursor.close()
          myconnect.close()

     except mysql.connector.Error as e:
          print('Error',e)
     
     

main()