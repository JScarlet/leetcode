class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_list = list(pattern)
        str_list = str.split()
        if len(pattern_list) != len(str_list):
            return False
        if len(set(zip(pattern_list, str_list))) == len(set(pattern_list)) == len(set(str_list)):
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    pattern = "abba"
    str = "dog cat cat dog"
    print(solution.wordPattern(pattern, str))
