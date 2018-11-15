class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = 0
        rotate_dict = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
        for i in range(1, N+1):
            str_i = str(i)
            new_i = ''
            for each in str_i:
                if each in rotate_dict:
                    new_i += rotate_dict[each]
                else:
                    new_i = str_i
                    break
            # print(str_i, new_i)
            if str_i != new_i:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.rotatedDigits(10))
