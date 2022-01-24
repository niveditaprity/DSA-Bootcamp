class Solution:
    def findK(self, a, n, m, k):
        # Your code goes here
       ans=[]
       left=0
       right=m-1
       up=0
       down=n-1
       c=0
       while(len(ans)<n*m):
           for i in range(left,right+1):
               c+=1
               ans.append(a[up][i])
               if c==k:
                   return ans[c-1]
           for j in range(up+1,down+1):
               c+=1
               ans.append(a[j][right])
               if c==k:
                   return ans[c-1]
           if up!=down:
               for i in range(right-1,left-1,-1):
                   c+=1
                   ans.append(a[down][i])
                   if c==k:
                       return ans[c-1]
           if left!=right:
               for i in range(down-1,up,-1):
                   c+=1
                   ans.append(a[i][left])
                   if c==k:
                       return ans[c-1]
           up+=1
           right-=1
           down-=1
           left+=1
       return ans[k-1]   