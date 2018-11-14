class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        length = len(chars)
        final = chars.pop()
        count = 1
        for i in range(1, length):
            temp = chars.pop()
            if temp != final:
                if count != 1:
                    ss = list(str(count))
                    ss.insert(0, final)
                    ss.reverse()
                    for letter in ss:
                        chars.insert(0, letter)
                else:
                    chars.insert(0, final)
                count = 1
                final = temp
            else:
                count += 1
        if count != 1:
            ss = list(str(count))
            ss.insert(0, final)
            ss.reverse()
            for letter in ss:
                chars.insert(0, letter)
        else:
            chars.insert(0, final)
        return chars


if __name__ == '__main__':
    solution = Solution()
    chars = ["a","a","a","b","b","a","a"]
    print(solution.compress(chars))


# 解题思路：
# 从最后一位依次pop出元素，然后计算出count之后插入最前面
