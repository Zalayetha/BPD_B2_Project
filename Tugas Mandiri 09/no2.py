listA = [1,2,4,8]
listB = [16,32,64,128]

def jumlah():
     totalA = sum(listA)
     totalB = sum(listB)
     total = sum(listA+listB)
     print(f'''
Jumlah List A       : {totalA}
Jumlah List B       : {totalB}
Jumlah keduanya     : {total}
     ''')
     

jumlah()