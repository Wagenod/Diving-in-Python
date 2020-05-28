import sys


if __name__ == "__main__":
    a, b, c = (int(param) for param in sys.argv[1:4])
    D = b**2 - 4*a*c
    x1 = (-b + D**0.5)/(2*a)
    x2 = (-b - D**0.5)/(2*a)
    print(x1, x2, sep="\n")
