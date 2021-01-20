import math
def is_prime(n):
    if(n%6 == 1):
        print("maybe prime")
        return 0
    if(n%6 != 5):
        print("not prime")
        return 0
    for i in range(0, int(math.sqrt(n)/6) + 1):
        if(n%(6*i + 5) == 0):
            print("not prime")
            return (6*i + 5)
    print("prime")
    return 1

print(is_prime(185537))

