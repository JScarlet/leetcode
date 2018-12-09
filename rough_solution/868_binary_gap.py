class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary_n = bin(N)
        binary_str = str(binary_n)[2:]
        # print(binary_str)
        result = []
        for i in range(0, len(binary_str)):
            if binary_str[i] == '1':
                result.append(i)
        if len(result) <= 1:
            return 0
        else:
            max_dis = 0
            for i in range(0, len(result) - 1):
                temp = result[i+1] - result[i]
                if temp > max_dis:
                    max_dis = temp
            return max_dis


if __name__ == '__main__':
    solution = Solution()
    print(solution.binaryGap(8))