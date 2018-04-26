from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        while True:

            try:
                nums.remove(val)
            except ValueError:
                break

        return len(nums)

    def test(self):
        result = self.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
        print(result)


if __name__ == '__main__':
    Solution().test()
