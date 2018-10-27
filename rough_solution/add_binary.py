class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_list = []
        for i in reversed(range(0, len(a))):
            a_list.append(int(a[i]))

        b_list = []
        for i in reversed(range(0, len(b))):
            b_list.append(int(b[i]))

        # short_length = min(len(a_list), len(b_list))
        if len(a_list) > len(b_list):
            short_list = b_list
            long_list = a_list
        else:
            short_list = a_list
            long_list = b_list
        result = []
        flag = False
        for i in range(0, len(short_list)):
            if not flag:
                single_sum = (short_list[i] + long_list[i])
            else:
                single_sum = (short_list[i] + long_list[i] + 1)
            temp = single_sum % 2
            result.append(temp)
            if single_sum // 2 > 0:
                flag = True
            else:
                flag = False

        for i in range(len(short_list), len(long_list)):
            if flag:
                single_sum = long_list[i] + 1
                temp = single_sum % 2
                result.append(temp)
                if single_sum // 2 > 0:
                    flag = True
                else:
                    flag = False
            else:
                result.append(long_list[i])

        if flag:
            result.append(1)

        final_result = ''
        for each in result[::-1]:
            final_result += str(each)
        return final_result


if __name__ == "__main__":
    solution = Solution()
    a = "1010"
    b = "1011"
    print(solution.addBinary(a, b))


# 解题思路：
# 先把字符串每一位存起来，然后每一位分别计算
# 或者直接用python将字符串转换为二进制数字然后换算成十进制计算后再转换