import sys


def main():
    sequence = []
    for line in sys.stdin:
        number = int(line)
        if number == -2_000_000_000:
            break
        sequence.append(number)

    numbers_pairs = list(zip(sequence, sequence[1:]))

    if all(x == y for x, y in numbers_pairs):
        print("CONSTANT")
    elif all(x < y for x, y in numbers_pairs):
        print("ASCENDING")
    elif all(x <= y for x, y in numbers_pairs):
        print("WEAKLY ASCENDING")
    elif all(x > y for x, y in numbers_pairs):
        print("DESCENDING ")
    elif all(x >= y for x, y in numbers_pairs):
        print("WEAKLY DESCENDING")
    else:
        print("RANDOM")


if __name__ == '__main__':
    main()
