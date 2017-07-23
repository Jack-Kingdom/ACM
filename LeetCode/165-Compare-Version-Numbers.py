def compare_lst(a,b):
    a=list(map(int,a))
    b=list(map(int,b))

    maxlen = max(len(a),len(b))
    for i in range(maxlen):
        if i is len(a):
            a.append(0)
        if i is len(b):
            b.append(0)

        if a[i]>b[i]:
            return 1
        elif a[i]<b[i]:
            return -1
    return 0

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        return compare_lst(v1,v2)

if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion('1.0','1'))
