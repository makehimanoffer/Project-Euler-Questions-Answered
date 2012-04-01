

plist = [2]

def primes(min, max):
    if 2 >= min: yield 2
    for i in range(3, max, 2):
        for p in plist:
            if i%p == 0 or p*p > i: break
        if i%p:
            plist.append(i)
            if i >= min: yield i
        
def factors(number):
    for bla in primes(2, number):
        if number % bla == 0:
            number /= bla
            yield bla
        if number == 1:
            break

print (max(factors(600851475143)))
