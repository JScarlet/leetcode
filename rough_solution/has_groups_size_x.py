class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        num_map = {}
        for each in deck:
            if each not in num_map:
                num_map[each] = 1
            else:
                num_map[each] += 1

        sorted_num = sorted(num_map.items(), key=lambda x:x[1])
        if sorted_num[0][1] < 2:
            return False

        num_list = [sorted_num[i][1] for i in range(0, len(sorted_num))]
        if len(num_list) <= 1:
            return True

        while num_list[-2] != 0:
            divisor = 0
            for i in range(0, len(num_list)):
                if num_list[i] != 0:
                    divisor = i
                    break
            for i in range(0, len(num_list)):
                if i != divisor:
                    num_list[i] = num_list[i] % num_list[divisor]
            num_list.sort()
        if num_list[-1] >= 2:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    deck = [1,1,2,2,2,2]
    print(solution.hasGroupsSizeX(deck))


# 解题思路：
# 先把数字以及出现次数放到字典中，然后求出所有数的最大公约数，如果比2大的话就返回true，否则返回false
