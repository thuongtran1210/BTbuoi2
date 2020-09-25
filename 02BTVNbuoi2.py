n = int(input("Nhập n nguyên dương: "))
x = float(input("Nhập x số thực bất kì: "))
s=0
it=1
for i in range (1,n+1):
    it = it *x
    s =s +it
print("S1: "+str(s+1))  
s2 = 0
for i in range(1,n+1):
    if i == n+1:
        s2 = (-1)**i*(x**i)
    else:
        if i%2==0:
            s2+= x**i
        else:
            s2-= x**i
print("S2 = ", 1+s2)


    
    

