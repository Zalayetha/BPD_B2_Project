print('''
========================================================
========================================================
========================================================
                                                       
***********  * * * * * * *    * * * * * * * *    *    
          *  *                *                 
          *  *                *                  *
          *  *                *                  *
          *  *                *                  *
          *  *                *                  *
          *  * * * * * * *    *     * * * * *    *   
          *  *                *     *       *    *
          *  *                *             *    * 
          *  *                *             *    *
       *     *                *             *    *
     *       *                *             *    *
   *         *                *             *    *
*            * * * * * * *    * * * * * * * *    *

========================================================
========================================================
========================================================

''')


def sum_nilai():
     i = True
     list_tugas = []
     while i == True :
          print('''
     **************************************
          PROGRAM HITUNG NILAI MAHASISWA
     **************************************

     **************************************
          ''')
          try:
               uts = int(input("Masukan nilai UTS : "))
               uas = int(input("Masukan Nilai UAS : "))
               quiz = int(input("Masukan Nilai QUIZ : "))
               banyak_tugas = int(input("Masukan Banyak Tugas : "))
               for i in range (banyak_tugas):
                    tugas = int(input(f"Masukan Nilai Tugas ke-{i+1} : "))
                    list_tugas.append(tugas)
      
               total_tugas = sum(list_tugas)
               #proses
               avg_tugas = round(total_tugas/banyak_tugas,1)
               nilai_akhir =(uts+uas+quiz+avg_tugas)//4

               print(f"Rata-Rata Nilai Tugas    : {avg_tugas}")
               print(f"Nilai Akhir    : {nilai_akhir}")

               if nilai_akhir >= 85:
                    print('Nilai Indeks   : A')
                    print('Nilai Predikat :BAIK SEKALI')
               elif nilai_akhir < 85 and nilai_akhir >= 60:
                    print('Nilai Indeks   : B')
                    print('Nilai Predikat : BAIK')
               elif nilai_akhir < 60:
                    print('Nilai Indeks   : C')
                    print('Nilai Predikat : KURANG BAIK')

               for i in range (banyak_tugas):
                    list_tugas.pop(0)

          except Exception :
               print("Data yang anda input salah,silakan dicoba lagi.")

                        
          ulang = input('nah COBA LAGI(y/t)? ')
          if ulang in ('y'):
               i = True
          elif ulang in ('t'):
               i = False
          else :
               print('ERROR!!!')
               i = False
               
sum_nilai()
