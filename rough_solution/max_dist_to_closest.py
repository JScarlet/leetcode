class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if len(seats) <= 1:
            return 0

        zero_count = 0
        zero_count_list = []

        for i in range(0, len(seats)):
            if seats[i] == 0:
                zero_count += 1
            else:
                zero_count_list.append(zero_count)
                zero_count = 0
        zero_count_list.append(zero_count)

        print(zero_count_list)
        if seats[0] != 1 and seats[-1] != 1:
            return max(zero_count_list[0], (sorted(zero_count_list, reverse=True)[0]+1)//2, zero_count_list[-1])
        elif seats[0] != 1 and seats[-1] == 1:
            return max(zero_count_list[0], (sorted(zero_count_list, reverse=True)[0] + 1) // 2)
        elif seats[0] == 1 and seats[-1] != 1:
            return max(zero_count_list[-1], (sorted(zero_count_list, reverse=True)[0] + 1) // 2)
        else:
            return (sorted(zero_count_list, reverse=True)[0] + 1) // 2


if __name__ == "__main__":
    solution = Solution()
    seats = [1,0,0,0,1,0,1]
    print(solution.maxDistToClosest(seats))

# 解题思路：
# 如果两端不是0的话，就是两个1之间0的个数的一半；
# 如果两端是0的话就比较两个1之间0的一半和这两端0的个数大小，返回大的即可
