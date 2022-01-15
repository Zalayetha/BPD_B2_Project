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

               hasil = kursor.fetchall() # menangkap semua data dari cursor dengan method fetchall()
               print('{} data yang diambil'.format(kursor.rowcount))

               # mengekstrak data di setiap baris 
               for row in hasil :

                    kode = row[0] # kolom ke-1 result set
                    judul = row[1] # kolom ke-2 result set
                    harga = row[2] # kolom ke-3 result set
                    penerbit = row[3] # kolom ke-4 result set
                    tahun = row[4] # kolom ke-5 result set

                    # menampilkan hasil ke layar 
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