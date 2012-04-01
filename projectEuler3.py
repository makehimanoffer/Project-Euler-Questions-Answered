#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

#for this I'll have to run through all the numbers from it down and modulus it:
#then return the value and print it out.

                
                


number=600851475143
decrementer=number
boolean=0

    
    
    
while decrementer>0:
    print (decrementer)
    incrementer=2
    x=0
    while incrementer< decrementer:
        
        x=decrementer%incrementer
        if x==0:
            break
            
            
        incrementer=incrementer+1

    if incrementer==decrementer:
        print("Prime Factor: "+ str(decrementer))
        boolean=1
        break



    if boolean==1:
        print("this is the one: " + str(decrementer))
        break

    decrementer=decrementer-1


