# Membuka file

buka = open('data_mahasiswa.txt','r')

# Baca isi file
baca = buka.readlines()

for i in baca :
     print(i)


# Tutup File
buka.close()