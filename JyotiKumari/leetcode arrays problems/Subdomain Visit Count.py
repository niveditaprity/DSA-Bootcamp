class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for domain in cpdomains:
            temp = domain.split(" ")
            count = int(temp[0])
            words = temp[1].split(".")
            l = []
            n = len(words)
            for i in range(n-1,-1,-1):
                if(i==n-1):
                    l.append(words[i])
                else:
                    l.insert(0,".")
                    l.insert(0,words[i])
                subdomain = "".join(l)
                if(subdomain in d):
                    d[subdomain]+=count
                else:
                    d[subdomain] = count
        l = []
        for key in d:
            temp = []
            temp.append(str(d[key]))
            temp.append(" ")
            temp.append(key)
            l.append("".join(temp))
        return l
        