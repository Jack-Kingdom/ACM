class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num = set()
        result =[]
        for i in nums:
            if i not in num:
                num.add(i)
            else:
                result.append(i)
        length = len(nums)
        for i in range(1,length+1):
            if i not in num:
                result.append(i)
        return result

if __name__ == '__main__':
    s = Solution()
    rst = s.findErrorNums([1,2,2,4])
    print(rst)