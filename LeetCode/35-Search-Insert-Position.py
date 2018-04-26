from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0

        length = len(nums)
        mid = length // 2

        if nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        if nums[mid] < target:
            return mid + 1 + self.searchInsert(nums[mid + 1:], target)
        else:
            return mid

    def test(self):
        data = [1, 3, 5, 6]
        result = self.searchInsert(data, 7)
        print('result:', result)


if __name__ == '__main__':
    Solution().test()
