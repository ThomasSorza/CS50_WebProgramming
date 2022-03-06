from functions import square #(import only the function from other file)
import functions #import the full module

for i in range(6):
    print(f"The square of {i} is {functions.square(i)}")