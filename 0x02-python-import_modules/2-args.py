#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        print("{0} argument:".format(len(argv) - 1))
        print("1: {}".format(argv[1]))
    elif len(argv) == 1:
        print("{0} arguments.".format(len(argv) - 1))
    else:
        print("{0} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{0}: {1}".format(i + 1, argv[i + 1]))
