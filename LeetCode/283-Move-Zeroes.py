from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        for _ in range(count):
            nums.append(0)

    def test(self):
        data = [0, 1, 2, 2, 3, 0, 4, 2]
        self.moveZeroes(data)
        print(data)


if __name__ == '__main__':
    Solution().test()
