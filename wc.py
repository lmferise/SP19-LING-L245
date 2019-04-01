import sys
#Sylable counter
counterspace = 0
countersyl = 0
counterchar = 0
counterline = 0
for c in sys.stdin.read():
    counterchar = counterchar +1
    if c == ' ' :
        counterspace = counterspace + 1
    if c in 'aeiou' :
        countersyl = countersyl + 1
    if c == "\n" :
        counterline = counterline + 1
print(counterspace)
print(countersyl)
average =  countersyl / counterspace
print (average)

print (counterchar)
print (counterline)
#This method might nnot be totally accurate because vowels such as "y" in english are situational. Also some languages may have sylables that do not include vowels and such. 
