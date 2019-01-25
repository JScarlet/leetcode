class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        x_list = []
        i = 0
        if x == 1:
            if x <= bound:
                x_list.append(1)
        else:
            while True:
                temp = x ** i
                if temp <= bound:
                    x_list.append(temp)
                    i += 1
                else:
                    break
        # print(x_list)
        y_list = []
        if y == 1:
            y_list = [x + 1 for x in x_list if x+1 <= bound]
        else:
            for j in range(0, len(x_list)):
                m = 0
                while True:
                    temp = x_list[j] + y ** m
                    if temp <= bound:
                        y_list.append(temp)
                        m += 1
                    else:
                        break
        # print(y_list)
        return list(set(y_list))


if __name__ == '__main__':
    solution = Solution()
    x = 2
    y = 3
    bound = 10
    print(solution.powerfulIntegers(x, y, bound))