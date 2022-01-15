# buka file 
file_puisi = open("puisi.txt","r")

# baca isi file 
puisi = file_puisi.readlines()

# cetak baris pertama
print(puisi[0])
# cetak baris kedua 
print(puisi[1])


# tutup file
file_puisi.close()