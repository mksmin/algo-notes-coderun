import sys


def main():
    n = int(input())
    array_nums = list(map(int, input().split()))

    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if array_nums[j] < array_nums[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_len = max(dp)
    last_index = dp.index(max_len)

    lis = []
    while last_index != -1:
        lis.append(array_nums[last_index])
        last_index = prev[last_index]

    lis.reverse()
    print(*lis)


if __name__ == '__main__':
    main()
