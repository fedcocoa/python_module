import csv

def counting(i):
    print(i)
    i=i+1
    if i ==100: return
    counting(i)

def countingReverse(i):
    print(i)
    i=i-1
    if i == 0: return
    countingReverse(i)

def doubles(i):
    print(i)
    if i != 1024:
        doubles(i*2)
    else:
        return

def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

'''question 3: Because pop will remove the items from the list, printing the list twice will result
in the list being empty the second time.
'''

# with open('facup.csv') as csvfile:
#     rdr = csv.reader(csvfile)
#     for row in rdr:
#             print(f"{row[0]} last won in {row[1]} {str(type(row[1]))}")

# with open('facup.csv') as csvfile:
#     rdr = csv.reader(csvfile)
#     for row in rdr:
#             print(int(row[1])%2 == 0)

def tour():
    reader = csv.reader(open('MultipleTourWinners.csv'))
    for row in reader:
        if row[1] == "FRA":
            print(f"{row[0]} {row[2]}")

# for n in range(100,200):
#     print(n)

# for n in range(0,102,2):
#     print(n)

def enumTour():
    reader = csv.reader(open('MultipleTourWinners.csv'))
    for i, row in enumerate(reader):
        if int(row[2]) >= 3:
            print(f"{i} : {row[0]}")


mark = input("enter mark: ")
if mark <= 50:
    print("Result is 2:2")

for n in range(1,10):
    print(n**2)

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)