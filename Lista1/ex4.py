def is_prime(n):
    for i in range(2,n):
        if n % i == 0: 
            print(False)
            return False
    print(True)
    return True

#examples: 

is_prime(2)
is_prime(3)
is_prime(25)
is_prime(37)
is_prime(81)