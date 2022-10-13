t=[]
p=[]
r=int(input("enter no. of numbers in tuple:"))
for i in range(r):
    x=int(input("enter no."))
    t.append(x)
for i in range(r):
    a=t[i]%10
    if a==0:
        p.append(t[i])
t=tuple(t)
print("tuple =",t)
p=tuple(p)
print("divisible by 5 and 2 =",p)
print("thanks")
