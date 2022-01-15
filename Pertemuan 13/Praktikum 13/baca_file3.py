# buka file 
file_puisi = open("Puisi.txt","r")

# baca isi file 
puisi = file_puisi.readlines()

# cetak isi file dengan perulangan 
for teks in puisi :
     print(teks)


# tutup file
file_puisi.close()