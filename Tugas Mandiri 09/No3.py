def Aritmatika(A,B,N):
     i = 1
     print('Deret Aritmatika  : ',end=" ")
     print(A,end=" ")
     for i in range (N-1):
          A+=B
          print(A,end=" ")

suku_awal = int(input('Masukan Suku Awal     : '))
beda_suku = int(input('Masukan Sentang Setiap Suku     : '))
banyak_suku = int(input('Masukan Banyak Suku     : '))

Aritmatika(suku_awal,beda_suku,banyak_suku)