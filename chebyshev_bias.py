import math
import copy 
from collections import defaultdict
def create_list_of_primes(n):
    primes = []
    for num in range(3,n,2):
        print(num)
        if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
            primes.append(num)
    return primes

def create_list_of_semiprimes(primes):
    semiprimes = []
    for i in range(0,len(primes)):
        for j in range(i, len(primes)):
            print(i)
            k = primes[i] * primes[j] 
            if(k < primes[-1]):
                semiprimes.append(k)
            else:
                break
    return semiprimes
one = []
three = []
five = []
seven = []
nine = []
eleven = []
thirteen = []
fifteen = []
seventeen = []
nineteen = []

size = 100000
primes = create_list_of_primes(size)

#comment out when not dealing with semiprimes
#semiprimes = create_list_of_semiprimes(primes)
#comment out when not graphing
#semiprimes.sort()
#both = primes + semiprimes
def number(n,array):
    iterations = 0
    for num in array:
        iterations += 1
        if((num - 1)%n == 0):
            one.append(num)
        elif((num - 3)%n == 0):
            three.append(num)
        elif((num - 5)%n == 0):
            five.append(num) 
        elif((num - 7)%n == 0):
            seven.append(num)  
        elif((num - 9)%n == 0):
            nine.append(num)   
        elif((num - 11)%n == 0):
            eleven.append(num)
        elif((num - 13)%n == 0):
            thirteen.append(num)   
        elif((num - 15)%n == 0):
            fifteen.append(num)  
        elif((num - 17)%n == 0):
            seventeen.append(num)  
        elif((num - 19)%n == 0):
            nineteen.append(num)  
        print(iterations) 
number(4, primes)
print("one      :" + str(len(one)))
print("three    :" + str(len(three)))
print("five     :" + str(len(five)))
print("seven    :" + str(len(seven)))
print("nine     :" + str(len(nine)))
print("eleven   :" + str(len(eleven)))
print("thirteen :" + str(len(thirteen)))
print("fifteen  :" + str(len(fifteen)))
print("seventeen:" + str(len(seventeen)))
print("nineteen :" + str(len(nineteen)))
print(len(primes))
#print(len(semiprimes))
def find_trend(n,array):
    #text_file = open(fileName, "w+")
    seen = 0
    trend = []
    output = []
    j = len(array)
    for i in range(n):
        if(j ==0):
            trend.append(seen)
        elif(i == array[0]):
            j -= 1
            seen+=1
            array.pop(0)
        trend.append(seen)
        output.append(seen)
        #text_file.write(str(seen) + ";")
    #text_file.close()
    with open(fileName, 'w') as f:
        for x in output:
            f.write("%d\n" % x)

    return trend
fileName = 'assembly.txt'
find_trend(size,one)
fileName = 'assembly3.txt'
find_trend(size,three)
'''
fileName = 'assembly2.txt'
find_trend(size,five)
print(find_trend(1000,fifteen))
print(find_trend(1000,five))
print(find_trend(1000,three))
text_file = open(fileName, "w")
text_file.write(print(find_trend(1000,fifteen)))
text_file.close()
'''