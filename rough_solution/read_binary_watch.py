class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        if num >= 9:
            return []
        hours_seq = {}
        for i in range(0, 2 ** len(hours)):
            temp = str(bin(i))[2:]
            while len(temp) < len(hours):
                temp = '0' + temp
            count = temp.count('1')
            if count not in hours_seq:
                hours_seq[count] = [temp]
            else:
                hours_seq[count].append(temp)

        minutes_seq = {}
        for i in range(0, 2 ** len(minutes)):
            temp = str(bin(i))[2:]
            while len(temp) < len(minutes):
                temp = '0' + temp
            count = temp.count('1')
            if count not in minutes_seq:
                minutes_seq[count] = [temp]
            else:
                minutes_seq[count].append(temp)
        print(hours_seq)

        result = []
        for i in range(0, min(3, num) + 1):
            other = abs(num) - i
            if other <= len(minutes):
                hours_seq_list = hours_seq[i]
                minutes_seq_list = minutes_seq[other]

                for each_hour in hours_seq_list:
                    hour_num = 0
                    for m in range(0, len(each_hour)):
                        if each_hour[m] == '1':
                            hour_num += hours[m]

                    for each_minute in minutes_seq_list:
                        minute_num = 0
                        for n in range(0, len(each_minute)):
                            if each_minute[n] == '1':
                                minute_num += minutes[n]
                        if hour_num <= 11 and minute_num <= 59:
                            hour_num_str = str(hour_num)
                            if minute_num < 10:
                                minute_num_str = '0' + str(minute_num)
                            else:
                                minute_num_str = str(minute_num)
                            result.append(hour_num_str + ':' + minute_num_str)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.readBinaryWatch(8))