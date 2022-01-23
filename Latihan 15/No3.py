# Latihan 15
# Merge Sort (Descending)

def Merge_Sort(list):

     print(f'Memecah {list}')
     n = len(list)
     if n < 2:
          return list 
     else :
          middle = n//2
          left = list[:middle]
          right = list[middle:]

          Merge_Sort(left)
          Merge_Sort(right)

          a = 0
          b = 0
          c = 0

          #looping
          while a < len(left) and b < len(right):
               if left[a] > right[b]:
                    list[c] = left[a]
                    a += 1 
               else:
                    list[c] = right[b]
                    b += 1
               c +=1
          while a < len(left):
               list[c] = left[a]
               a +=1
               c +=1
          while b < len(right):
               list[c] = right[b]
               b+=1
               c+=1
     print(f'Menggabungkan {list}')




mylist = [32,16,42,-5,33,12,14,-9,11,16]
print('\n\t\t\t Merge Sort (Descending)\n')
print(f'\nData sebelum diurutkan : {mylist}')
print(f'\nProses Pengurutan : \n')
Merge_Sort(mylist)
print(f'\nData setelah diurutkan : {mylist}\n')
