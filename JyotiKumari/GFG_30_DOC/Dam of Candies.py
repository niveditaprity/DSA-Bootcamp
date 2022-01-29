class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        if(n==1 or n==2):
            return 0
        front = 0
        tail = n-1
        ans=0
        while(front<tail):
            ans = max(ans, (tail-front-1)*(min(height[front], height[tail])))
            if height[front]>height[tail]:
                tail-=1
            elif height[front]<height[tail]:
                front+=1
            else:
                front+=1
                tail-=1
        return ans