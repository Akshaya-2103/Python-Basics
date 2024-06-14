'''from collections import Counter
import operator
d = {}
d1 = {}
n = int(input())
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v
m = int(input())
for i in range(m):
    k = input()
    v = int(input())
    d1[k]=v
#d2 = Counter(d) + Counter(d1)
#print(d2)
d3 = d.copy()
for i in d1.keys():
    if i in d3:
        d3[i] = d.get(i)+d1.get(i)
    else:
        d3[i] = d1.get(i)
print(d3)
'''

d = {}
ans=[]
nums=[8,1,2,2,3]
a = sorted(nums)
for i in range(len(nums)):
    if a[i] not in d:
        d[a[i]] = i
print(d)
for i in range(len(nums)):
    ans.append(d[nums[i]])
print(ans)
#1365