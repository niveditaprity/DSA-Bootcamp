#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        plst=[]
        nlst=[]
        for i in arr:
            if(i>=0):
                plst.append(i)
            else:
                nlst.append(i)
        j=0
        for i in range(len(plst)):
            arr[i]=plst[i]
            j+=1
        for i in range(len(nlst)):
            arr[j]=nlst[i]
            j+=1
            
        # Your code goes here

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
