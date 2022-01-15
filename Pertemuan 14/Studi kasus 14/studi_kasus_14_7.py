import mysql.connector
import sys

def main():
     try:
          # saya tidak mencantumkan password untuk user root dikarenakan credential dari root saya tidak memiliki password 
          koneksi = mysql.connector.connect(
               user='root',host='localhost',database='dbpenjualan'
          )
          sql = ('SELECT * FROM buku ORDER BY kode')
          try:
               kursor = koneksi.cursor()
               kursor.execute(sql)

               row= kursor.fetchone() # menangkap semua data dari cursor dengan method fetchone()
               print('{} data yang diambil'.format(kursor.rowcount))

               print('Menggunakan fetchone()')

               # menampilkan hasil ke layar 
               print(row[0],'\t',
                    row[1],'\t',
                    row[2],'\t',
                    row[3],'\t',
                    row[4])
          except:
               print('pengambil data gagal...')
               sys.exit()
          
          else:
               koneksi.close
     
     except mysql.connector.Error as e:
          print('Error',e)
     else:
          koneksi.close

if __name__=="__main__":
     main()