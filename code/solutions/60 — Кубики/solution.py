import sys


def main():
    count_numbers = list(map(int, input().split()))
    a_numbers = set()
    b_numbers = set()

    for _ in range(count_numbers[0]):
        i = int(input())
        a_numbers.add(i)

    for _ in range(count_numbers[1]):
        i = int(input())
        b_numbers.add(i)

    common = sorted(a_numbers & b_numbers)
    anna_nums = sorted(a_numbers - b_numbers)
    borya_nums = sorted(b_numbers - a_numbers)

    print(f"{len(common)}")
    print(f"{" ".join(map(str, common))}")

    print(f"{len(anna_nums)}")
    print(f"{" ".join(map(str, anna_nums))}")

    print(f"{len(borya_nums)}")
    print(f"{" ".join(map(str, borya_nums))}")


if __name__ == '__main__':
    main()