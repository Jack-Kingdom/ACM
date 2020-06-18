from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = [0 for _ in range(101)]
        for i in nums:
            counter[i] += 1

        return [sum(counter[:i]) for i in nums]
