class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_set = set(list(s))
        t_set = set(list(t))
        if len(s_set) > len(t_set):
            return ''.join(s_set - t_set)
        elif len(s_set) < len(t_set):
            return ''.join(t_set - s_set)
        else:
            for each in s_set:
                if s.count(each) != t.count(each):
                    return each
            return None


if __name__ == '__main__':
    solution = Solution()
    s = "abcde"
    t = "abcde"
    print(solution.findTheDifference(s, t))
