import sys
#token counter
counter = 0
countersyl = 0

for c in sys.stdin.read():
    if c == ' ' :
        counter = counter + 1
    if c in 'aeiou' :
        countersyl = countersyl + 1
print(counter)
print(countersyl)
average =  countersyl / counter
print (average)
