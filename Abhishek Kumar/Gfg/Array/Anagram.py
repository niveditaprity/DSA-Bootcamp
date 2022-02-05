    def isAnagram(self,a,b):
       
        if len(a) != len(b):
            return False
        
        else:
            a = list(a)
            b = list(b)
            
            a.sort()
            b.sort()
            
            n = len(a)
            
            for i in range(n):
                if a[i] != b[i]:
                    return False
            return True
