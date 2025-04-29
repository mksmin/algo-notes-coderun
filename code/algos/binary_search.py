"""
Найти позицию для вставки
Дано отсортированное множество различных целых чисел и целевое значение, вернуть индекс, если цель найдена. Если нет,
вернуть индекс, где бы он был, если бы он был вставлен по порядку
Необходимо написать алгоритмы обладающий O(log n) сложностью во время выполнения

Пример 1:
Ввод: nums = [1,3,5,6], target = 5
Вывод: 2

Пример 2:
Ввод: nums = [1,3,5,6], target = 2
Вывод: 1

Пример 1:
Ввод: nums = [1,3,5,6], target = 7
Вывод: 4
"""


class Solution:
    def insert_search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mdl = (l + r) // 2

            if nums[mdl] == target:
                return mdl

            elif nums[mdl] < target:
                l = mdl + 1

            else:
                r = mdl - 1

        return l


nums = [1, 3, 5, 6]
target = 5
sol = Solution()

print(nums, target)
print(sol.insert_search(nums, target))

target = 2
print(nums, target)
print(sol.insert_search(nums, target))

target = 7
print(nums, target)
print(sol.insert_search(nums, target))

if __name__ == '__main__':
    pass
