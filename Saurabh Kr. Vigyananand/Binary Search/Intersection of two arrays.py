class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst=[]
        n1=list(set(nums1))
        n2=list(set(nums2))
        i=0
        while(i<len(n1)):
            for j in range(0,len(n2)):
                if(n1[i]==n2[j]):
                    lst.append(n1[i])
            i+=1
        return lst
                
