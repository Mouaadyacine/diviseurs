a=int(input("entrer un entier"))
b=0
c=""
for i in range(1,-1):
 if a%i==0:
    b=b+1
    c=c+i
print(b)
print(c)