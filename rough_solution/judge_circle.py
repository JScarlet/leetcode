class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        move_dict = {}
        for each in moves:
            if each not in move_dict:
                move_dict[each] = 1
            else:
                move_dict[each] += 1
        ud_flag = False
        if 'U' in move_dict and 'D' in move_dict:
            if move_dict['U'] == move_dict['D']:
                ud_flag = True
        elif 'U' not in move_dict and 'D' not in move_dict:
            ud_flag = True

        lr_flag = False
        if 'L' in move_dict and 'R' in move_dict:
            if move_dict['L'] == move_dict['R']:
                lr_flag = True
        elif 'L' not in move_dict and 'R' not in move_dict:
            lr_flag = True

        if ud_flag and lr_flag:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    moves = "LL"
    print(solution.judgeCircle(moves))
