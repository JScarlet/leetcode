class Solution:
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result_set = set()
        for each in A:
            if len(each) == 1:
               result_set.add(each)
            else:
                odd_list = tuple(sorted(list(each[0::2])))
                even_list = tuple(sorted(list(each[1::2])))
                result_set.add((odd_list, even_list))
        return len(result_set)


if __name__ == '__main__':
    solution = Solution()
    A = ["abcd","cdab","adcb","cbad"]
    print(solution.numSpecialEquivGroups(A))


# 解题思路：
# 只需比较每个字符串的奇数位和偶数位排序后是否相等，如果都相等的话即为特殊等价字符串组
