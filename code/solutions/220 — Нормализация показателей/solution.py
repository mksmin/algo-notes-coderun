import sys

class Solution:
    def insert_search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1

            else:
                r = mid

        return l


def main():
    n = int(input())
    n_nums = sorted(map(int, input().split()))
    m = int(input())

    sol = Solution()

    for _ in range(m):
        target = int(input())
        index = sol.insert_search(n_nums, target)

        if index == 0:
            answer = n_nums[0]

        else:
            left = n_nums[index - 1]
            right = n_nums[index]

            if abs(target - left) <= abs(target - right):
                answer = left
            else:
                answer = right

        print(answer)

if __name__ == '__main__':
    main()