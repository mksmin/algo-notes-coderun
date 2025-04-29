import sys


class Solution:
    def insert_search(self, nums: list[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mdl = (l + r) // 2

            if target == nums[mdl]:
                return True

            elif target > nums[mdl]:
                l = mdl + 1

            else:
                r = mdl - 1

        return False


def main():
    first_line = input()
    first_arr = sorted(list(map(int, input().split())))
    second_arr = list(map(int, input().split()))

    sol = Solution()

    for i in second_arr:
        result = sol.insert_search(first_arr, i)
        if result:
            print('YES')
            continue
        print("NO")


if __name__ == '__main__':
    main()
