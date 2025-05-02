import sys

class Solution:
    def insert_search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l

def main():
    N = input()
    n_nums = sorted(set(map(int, input().split())))
    K = input()
    k_nums = list(map(int, input().split()))

    sol = Solution()
    for i in k_nums:
        result = sol.insert_search(n_nums, i)
        print(result)


if __name__ == '__main__':
    main()