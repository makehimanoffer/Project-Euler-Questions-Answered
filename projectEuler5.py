def LCM(a,b):
    num1=a
    num2=b
    while a!=b:
        if a<b:
            a+=num1
        else:
            b+=num2
    return a

	
num = 1
limit = 20 
i=2	
print("This program will find out the least number which is divisible by all numbers from 1 to "+ str(limit));
while i<=limit:	
	num=LCM(num,i)
	i=i+1	
print("The answer is: "+ str(num))

	
