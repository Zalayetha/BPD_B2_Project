# Latihan 15
# Bubble Short (Descending)

def Bubble_Sort(list):
     iterasi = 0
     for j in range (len(list)-1):
          for i in range (len(list)-1-j):
               if list[i]<list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
          iterasi += 1
          print(iterasi,list)

mylist = [15,10,-7,22,17,5,12,-1,9]
print('\n\t\t\t Bubble Sort (Descending)\n')
print(f'\nData sebelum diurutkan : {mylist}')
print(f'\nProses Pengurutan : \n')
Bubble_Sort(mylist)
print(f'\nData setelah diurutkan : {mylist}\n')