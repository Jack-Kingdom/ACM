class Solution:
    def dominantIndex(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """

        order = sorted(nums, reverse=True)

        if len(nums) == 1:
            return 0
        else:
            first = order[0]
            second = order[1]

            if first >= 2 * second:
                return nums.index(first)
            else:
                return -1
