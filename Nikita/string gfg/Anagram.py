def isAnagram(self,a,b):
        if len(a)!=len(b):
            return 0
        if len(a)==len(b):
            if sorted(a)!=sorted(b):
                return 0
            elif sorted(a)==sorted(b):
                return 1
            
        #code here
