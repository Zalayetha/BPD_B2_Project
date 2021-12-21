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
list = []
i = 0
def InputData():
     global isi_data,n
     n = int(input('Masukan banyaknya data   : '))
     isi_data = int(input('Isi Data     : '))
     list.append(isi_data)

def proses():
     global isi_data,n,i
     for i in range (n):
          isi_data += isi_data
          list.append(isi_data)

def CetakHasil():
     global isi_data,n,i
     print('''
No.Indeks     Bilangan Genap    
     ''')
     for i in range (n) :
          print(f'  {i}                 {list[i]}')

InputData()
proses()
CetakHasil()
