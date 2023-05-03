def is_prime(x):
    for i in range(2,int(x/2)):
        if x % i == 0:
            return False
    return True

def get_primes():
    num = 2
    while num <= 10000:
        if is_prime(num):
            yield num
        num += 1

    
for i in get_primes():
        print(i)