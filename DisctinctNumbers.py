n = int(input())
l= sorted(list(map(int,input().split())))
c=0
m=int(0)
for i in range(n):
    if(not(l[i]==m)):
        m=l[i]
        c=c+1

print(c)