class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        result = ''
        i = 1
        while i * k <= len(s):
            if i % 2 != 0:
                # print(s[(i-1)*k: i*k:][::-1])
                result += s[(i-1)*k: i*k][::-1]
            else:
                result += s[(i-1)*k: i*k]
            i += 1
        if i % 2 != 0:
            result += s[(i-1)*k:][::-1]
        else:
            result += s[(i-1)*k:]
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "abcdefgh"
    k = 3
    print(solution.reverseStr(s, k))
