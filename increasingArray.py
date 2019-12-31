n= int(input())
l=list(map(int,input().strip().split()))
sum=0
a=l[0]
for i in range(1,n):
    
    b=l[i]
    if(b<a):
        sum=sum+abs((a-b))
    else:
        a=b

print(sum)
