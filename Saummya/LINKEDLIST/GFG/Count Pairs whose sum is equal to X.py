class Solution:
    def countPair(self,h1,h2,n1,n2,x):
        '''
        h1:  head of linkedList 1
        h2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:   len of linkedList 1
        X:   given sum
        '''
        
        temp1=h1
        temp2=h2
        count=0
        s=set()
        while temp1!=None:
            s.add(temp1.data)
            temp1=temp1.next
        while temp2!=None:
            if((x-temp2.data) in s):
                count+=1
            temp2=temp2.next
        return count
