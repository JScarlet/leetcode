class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bill_5 = 0
        bill_10 = 0
        bill_20 = 0
        for i in range(0, len(bills)):
            if bills[i] == 5:
                bill_5 += 1
            elif bills[i] == 10:
                if bill_5 > 0:
                    bill_5 -= 1
                    bill_10 += 1
                else:
                    return False
            else:
                if bill_5 > 0 and bill_10 > 0:
                    bill_5 -= 1
                    bill_10 -= 1
                    bill_20 += 1
                elif bill_5 >= 3:
                    bill_5 -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    bills = [5,5,10,10,20]
    print(solution.lemonadeChange(bills))
