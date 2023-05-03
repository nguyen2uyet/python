def is_prime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range (3,int(n/2),2):
                if n % i == 0:
                    return False    

    return True

a = int(input())

for i in range(a):
    number = int(input())
    if is_prime(number):
        print("Prime")
    else:
        print("Not prime")

