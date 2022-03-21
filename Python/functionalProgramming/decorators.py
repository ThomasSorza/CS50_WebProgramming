def announce(f):
    def wrapper():#takes a function and add more key habilities
        print("About to yun te function...")
        f()
        print("Done with the function.")
    return wrapper

@announce #anounnce decorator
def hello():
    print("Hello, world!")

hello()