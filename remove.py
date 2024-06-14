l = [4,5,6,7,8,9]
for i in l:
    l.remove(i)
print(l)

l = [2,3,4,5]
print(l[4:7])

for i in [2,4,6,8,10,12]:
    i = i+2
    print(i)

for i in [1,2,3,4,5,6,7,8]:
    i = i+10
    print(i)

n = int(input())
a,b = 0,1
for i in range(5):
    a,b = b,a+b
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b