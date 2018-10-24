class Solution:
    def myAtoi(self, str):
        result = ''
        num_count = 0
        symbol_count = 0
        for letter in str:
            if letter != ' ':
                if letter == '+' or letter == '-':
                    if num_count == 0:
                        result += letter
                        symbol_count += 1
                    else:
                        break
                elif letter.isnumeric():
                    num_count += 1
                    result += letter
                else:
                    break
            else:
                if num_count != 0 or symbol_count != 0:
                    break

        # result = self.operate_num(result)
        if symbol_count > 1:
            return 0

        if result == '' or result == '+' or result == '-':
            return 0
        else:
            num = int(result)
            if num > 2**31 - 1:
                return 2**31 - 1
            elif num < -2**31:
                return -2**31
            else:
                return num


if __name__ == "__main__":
    solution = Solution()
    print('1'.isnumeric())
    result = int('-91283472332')
    print(result)
    print(solution.myAtoi('"+-1"'))