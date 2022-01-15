import mysql.connector

def main():
     try:
          db_name = {'user':'root','host':'localhost','database':'dbpenjualan'}
          myconnect = mysql.connector.connect(**db_name)
          mycursor = myconnect.cursor()     
          sql = ('SELECT * FROM pegawai ORDER BY NIP')

          # execute 
          mycursor.execute(sql)
          
          # result menggunakan fetchall
          result = mycursor.fetchall()
          print(f'{mycursor.rowcount} data yang diambil')

          for row in result :
               nip = row[0]
               nama = row[1]
               jabatan = row[2]
               divisi = row[3]
               gaji = row[4]

               print(f'''
NIP       : {nip}
Nama      : {nama}
Jabatan   : {jabatan}
Divisi    : {divisi}
Gaji      : {gaji}
               ''')
          mycursor.close()
          myconnect.close()

     except mysql.connector.Error as e:
          print('Error',e)
     
     

main()