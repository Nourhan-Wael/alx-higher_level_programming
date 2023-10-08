#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    r = 0
    for i in range(len(argv) - 1):
        r += int(argv[i + 1])
    print(r)
