import mysql.connector
import sys

def main():
     try:
          # saya tidak mencantumkan password untuk user root dikarenakan credential dari root saya tidak memiliki password 
          koneksi = mysql.connector.connect(
               user='root',host='localhost',database='dbpenjualan')

          sql = ('SELECT * FROM buku ORDER BY kode')
          try:
               kursor = koneksi.cursor(buffered = True)
               kursor.execute(sql)

               hasil =  kursor.fetchmany(3) # menangkap semua data dari cursor fetchmany(n)
               print('{} data yang diambil'.format(kursor.rowcount))

               print('Menggunakan fetchmany(4):')

               # menampilkan hasil ke layar 
               for (kode,judul,harga,penerbit,tahun) in hasil:
                    print(kode,'\t',
                         judul,'\t',
                         harga,'\t',
                         penerbit,'\t',
                         tahun)
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