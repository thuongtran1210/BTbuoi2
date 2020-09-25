sum=0
n =int(input("Nhập N: "))
print("Từ 1 đến n: ",end='')
for i in range (1,n+1,1):
    if i==17:
        continue
    sum = sum +i
    print(i,end=' ')
print("= "+str(sum))