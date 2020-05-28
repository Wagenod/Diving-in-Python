import sys


if __name__ == "__main__":
    n_steps = int(sys.argv[1])
    for i_step in range(1, n_steps+1):
        print(" "*(n_steps-i_step) + "#"*i_step)
