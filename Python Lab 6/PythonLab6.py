import math

sports = ["football","rugby","hockey","tennis"]
print(f"{sports[0]} and {sports[len(sports)-1]}")
sports.append("cycling")
print(len(sports))

for sport in sports:
    print(sport[0])

sports.remove('football')

new_sports = sports[(len(sports)//2)-1:(len(sports)//2)+1]

#question 2
#Pop will remove the item at the index provided and return it however remove will remove the item with the value provided and does not return anything

letters=['a','b','c','d','e']
letters.pop(3)
letters.remove('a')

#question 3

def square(n):
    return n*n

square = lambda n : n*n

a = ["tim", "bob", "trevor", "susan", "anna"]
sorted(a,key=lambda x: x[0])
sorted(a,key=lambda x: x[1])
sorted(a,key=lambda x: x[len(x)-1])
sorted(a,key=lambda x: len(x))
sorted(a,key=lambda x: (len(x),x))
sorted(a,key=lambda x: (x[0] in ['a','e','i','o','u'],x))

#question 6
for x in range(0,10):
    print()
    for y in range(0,10):
        print("*",end='')

def asterisks(m,n):
    for x in range(0,m):
        print()
        for y in range(0,n):
            print("*",end='')

def pallets(weights):
    total = 0
    full = False
    while not full:
        current = weights.pop(0)
        if total+current >= 3000:
            full = True
        else:
            total+=current
            print(f"Total:{total} Current:{current}")
 
#question 8
def asterisks():
    m = input('Length:')
    n = input('Width:')
    for x in range(0,m):
        print()
        for y in range(0,n):
            print("*",end='')

#question 9
a = {1,2,3,4}
b = {3,4,5,6}

a.union(b)
a.intersection(b)
a-b
(a-b).union((b-a))
a.intersection(a)

#question 12
def printStarCircle(radius):
    for x in range(-radius,radius):
        print()
        for y in range(-radius,radius):
            if math.sqrt(x**2 + y**2) <= radius:
                print("*",end='')
            else:
                print(" ",end='')


#question 13

def pallets(weights):
    total = 0
    full = False
    for pallet in weights:
        current = weights.pop(0)
        if total+current <= 3000:
            total+=current
            print(f"Total:{total} Current:{current}")