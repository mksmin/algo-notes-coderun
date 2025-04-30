import sys


def main():
    N, K = map(int, input().split())
    nums = [int(input()) for _ in range(N)]

    l = 1
    r = max(nums)
    result = 0

    while l <= r:
        mid = (l + r) // 2
        pieces = sum(x // mid for x in nums)

        if pieces >= K:
            result = mid
            l = mid + 1
        else:
            r = mid - 1

    print(result)



if __name__ == '__main__':
    main()