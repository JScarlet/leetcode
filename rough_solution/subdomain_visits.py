class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_dict = {}
        for each in cpdomains:
            domain_times = each.split()
            times = int(domain_times[0])
            domain = domain_times[1]
            if domain not in domain_dict:
                domain_dict[domain] = times
            else:
                domain_dict[domain] += times
            while '.' in domain:
                dot_index = domain.find('.')
                domain = domain[dot_index+1:]
                if domain not in domain_dict:
                    domain_dict[domain] = times
                else:
                    domain_dict[domain] += times

        result = []
        for key in domain_dict:
            value = domain_dict[key]
            single = str(value) + ' ' + str(key)
            result.append(single)
        return result


if __name__ == '__main__':
    solution = Solution()
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(solution.subdomainVisits(cpdomains))
