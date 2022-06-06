def main():
    a = int(input("Enter 1st number?"))
    b = int(input("Enter 2nd number?"))
    c = add(a, b)
    print("Sum of a and b is", c)
    
def add(a,b):
    c = a+b
    return c

main()