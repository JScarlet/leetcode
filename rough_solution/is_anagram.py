class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_list = sorted([letter for letter in s])
        t_list = sorted([letter for letter in t])
        # print(s_list, t_list)
        if s_list == t_list:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))
