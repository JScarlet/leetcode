class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            if len(A) == len(set(list(A))):
                return False
            return True
        else:
            temp_a = []
            temp_b = []
            for i in range(0, len(A)):
                if A[i] != B[i]:
                    temp_a.append(A[i])
                    temp_b.append(B[i])
            if len(temp_b) == len(temp_a) == 2 and temp_b == temp_a[::-1]:
                return True
            return False


if __name__ == '__main__':
    solution = Solution()
    A = "aaaaaaabc"
    B = "aaaaaaacb"
    print(solution.buddyStrings(A, B))


# 解题思路：
# 如果两个字符串长度不相等的话，直接返回False；
# 如果两个字符串相等，里面含有重复元素的话为True，没有重复元素的话就为False
# 如果两个字符串不相等，如果两个字符串只有两个字符不相同且顺序刚好相反的话为True，否则就为False
