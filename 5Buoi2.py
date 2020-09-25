#Bai5
sum =0
n =int(input("Nhập N: "))
print("Từ 1 đến n: ",end='')
for i in range (1,n+1,1):
    sum = sum +i
    print(i,end=' ')
print("= "+str(sum))
print("TBC: "+str(sum/n))

