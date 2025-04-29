import sys

class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def insert_search(self, target: int):
        l = 0
        r = len(self.nums) - 1

        while l <= r:
            mdl = (l + r) // 2

            if target == self.nums[mdl]:
                return mdl

            if target > self.nums[mdl]:
                l = mdl + 1

            else:
                r = mdl - 1

        return l

    def find_closest(self, target: int):
        search_indx = self.insert_search(target)

        if search_indx == 0:
            return self.nums[0]

        elif search_indx >= len(self.nums):
            return self.nums[-1]

        else:
            left = self.nums[search_indx - 1]
            right = self.nums[search_indx]

            if abs(target - left) <= abs(right - target):
                return left
            return right


def main():
    skip_line = input()
    nums = list(map(int, input().split()))
    targets = list(map(int, input().split()))

    sol = Solution(nums=nums)

    for item in targets:
        print(sol.find_closest(target=item))


if __name__ == '__main__':
    main()