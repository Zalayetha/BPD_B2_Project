# Fungsi untuk menginput
def input_data():
     i =0
     jumlah = int(input('Input berapa data ? '))
     while i < jumlah :
          data = input('Masukan data anda : ')
          buka.write("\n")
          buka.write(data)
          i = i +1

# Membuka file
buka = open('data_mahasiswa.txt','r+')


# Input data 
input_data()

# Baca data
baca= buka.readlines()

# Tutup File
buka.close()