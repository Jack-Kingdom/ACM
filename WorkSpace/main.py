class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = len(nums)
        require = {}
        for i in range(total):

            if nums[i] in require:
                return [require[nums[i]], i]

            sub = target - nums[i]
            require[sub] = i
