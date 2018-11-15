class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 1
        while i < len(s):
            sub_list = []
            if len(s) % i == 0:
                times = len(s) // i
                # print(times)
                for j in range(1, times+1):
                    sub_list.append(s[(j-1)*i: j*i])
                # print(sub_list)
                if len(set(sub_list)) == 1:
                    return True
            i += 1
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "abcabcabcabc"
    print(solution.repeatedSubstringPattern(s))
