import sys


def main():
    data = sys.stdin.read()
    massive = data.split()
    new_massive = [int(x) for x in massive]
    new_massive.sort()

    print(new_massive[1])


if __name__ == '__main__':
    main()
