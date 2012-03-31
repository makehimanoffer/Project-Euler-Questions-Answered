#the aim of this program is to add up all the multiples of 3 and 5
#of which are natural numbers

i=0
sum=0
while i<1000:
    if i%3==0 and  i%5!=0:
        sum=sum+i
    i=i+1

i=0
while i<1000:
    if i%5==0 and i%3!=0:
        sum=sum+i
    i=i+1

i=0
while i<1000:
    if i%5==0 and  i%3==0:
       sum=sum+i
    i=i+1
       

print(sum)
    
#this has gotten the right answer on project euler as its output    
