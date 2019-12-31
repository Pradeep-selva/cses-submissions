s=input()

temp = s[0]
m=k=1
for i in range(1,len(s)):
    if(s[i]==temp):
        k=k+1
    else:
        m=max([m,k])
        k=1
        temp=s[i]


print(max([m,k]))
