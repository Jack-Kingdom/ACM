class Solution:
    def balancedStringSplit(self, s: str) -> int:
        rst, tmp = 0, 0

        for c in s:
            if c == 'R':
                tmp += 1
            if c == 'L':
                tmp -= 1

            if tmp == 0:
                rst += 1

        return rst
