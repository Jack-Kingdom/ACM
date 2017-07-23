class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        best = 0
        nums =set(nums)
        for num in nums:
            if num - 1 in nums:
                pass
            else:
                tester = num + 1
                while tester in nums:
                    tester +=1
                best = max(best,tester - num)
        return best
