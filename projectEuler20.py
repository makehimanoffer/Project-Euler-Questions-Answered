sum=1
i=100
add=0
while i>0:
    sum=sum*i
    i=i-1
    

thingy=str(sum)
i=0
a=0
while i<len(thingy):
    a=a+int(thingy[i])
    i=i+1
print(a)
