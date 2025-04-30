import sys


def main():
    nums = list(map(int, input().split()))
    w, h, n = nums
    l = s = 0
    r = 1

    while s < n:
        r *= 2
        s = (r//w)*(r//h)
    while l < r:
        mid = (l + r)//2
        if (mid//w)*(mid//h) >= n:
            r = mid
        else:
            l = mid + 1

    print(l)


if __name__ == '__main__':
    main()