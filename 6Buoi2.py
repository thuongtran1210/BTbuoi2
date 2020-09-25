#Bai6
sum=0
n =int(input("Nhập N: "))
print("Từ 1 đến n: ",end='')
for i in range (1,n+1,1):
    if i==13:
        break
    sum = sum +i
    print(i,end=' ')
print("= "+str(sum))