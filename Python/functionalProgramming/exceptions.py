import sys

try: #try to get the input
    x =int(input("x: "))
    y =int(input("y: "))
except ValueError: #ErrorName
    print("Error: invalid input.")
    sys.exit(1)

try:
    result = x / y 
except ZeroDivisionError:#ErrorName
    print("Error: cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")