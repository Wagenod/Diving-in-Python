import sys


if __name__ == "__main__":
    str_digits = list(map(lambda num: int(num), sys.argv[1]))
    print(sum(str_digits))

