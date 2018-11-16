class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for i in range(0, len(s)):
            if s[i] not in s_dict:
                s_dict[s[i]] = [i]
            else:
                s_dict[s[i]].append(i)

        for i in range(0, len(t)):
            if t[i] not in t_dict:
                t_dict[t[i]] = [i]
            else:
                t_dict[t[i]].append(i)

        print(sorted(s_dict.values()))
        print(sorted(t_dict.values()))
        s_index_list = sorted(s_dict.values())
        t_index_list = sorted(t_dict.values())
        if len(s_index_list) == len(t_index_list):
            for i in range(0, len(s_index_list)):
                if s_index_list[i] != t_index_list[i]:
                    return False
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s = "paper"
    t = "title"
    print(solution.isIsomorphic(s, t))
