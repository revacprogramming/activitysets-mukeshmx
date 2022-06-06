
def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    c = add(a,b)
    output(a, b, c)


def add(a, b):
    c = a+b
    return c


def output(a, b, c):
    print("ans %d and %d is %d" %  (a, b, c))
main()
