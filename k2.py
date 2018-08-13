num1,k=input().split()
num1=int(num1)
k=int(k)
a = [int(x) for x in input().split()]
s=0
for i in range(0,k):
    s+=a[i]
print(s)
