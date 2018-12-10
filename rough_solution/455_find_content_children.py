class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        sorted_g = sorted(g)
        sorted_s = sorted(s)
        i, j = 0, 0
        while i < len(sorted_g) and j < len(sorted_s):
            if sorted_g[i] <= sorted_s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    g = [1, 2]
    s = [1, 2, 3]
    print(solution.findContentChildren(g, s))
