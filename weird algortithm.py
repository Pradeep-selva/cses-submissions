
n = int(input())

if(not(n>=1 and n<=1000000)):
    exit()

print(n,end=' '),

while(n!=1):
    if(n%2==0):
        n=n/2
    else:
        n=(n*3)+1
    print(int(n),end=' '),
