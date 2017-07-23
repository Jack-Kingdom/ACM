class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for ps1, fst_num in enumerate(nums):
            for ps2, snd_num in enumerate(nums[ps1 + 1:], ps1+1):
                if fst_num + snd_num == target:
                    return [ps1, ps2]
