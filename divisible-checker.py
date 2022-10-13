t=[]
p=[]
r=int(input("Enter amount of numbers in tuple:"))
for i in range(r):
    x=int(input("Enter number"))
    t.append(x)
for i in range(r):
    a=t[i]%10
    if a==0:
        p.append(t[i])
t=tuple(t)
print("Tuple =",t)
p=tuple(p)
print("Divisible by 5 and 2 =",p)
print("Thanks for testing!")
