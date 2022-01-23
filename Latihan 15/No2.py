# Latihan 15
# Selection Sort (Descending)

def Selection_Sort(list):
     iterasi = 0
     for i in range(len(list)-1):
          max = i
          for j in range(i+1,len(list)):
               if list[j] > list[max] :
                    max = j
          iterasi += 1
          list[i],list[max] = list[max],list[i]
          print(iterasi,list)


mylist = [15,10,-7,22,17,5,12,-1,9]
print('\n\t\t\t Selection Sort (Descending)\n')
print(f'\nData sebelum diurutkan : {mylist}')
print(f'\nProses Pengurutan : \n')
Selection_Sort(mylist)
print(f'\nData setelah diurutkan : {mylist}\n')

