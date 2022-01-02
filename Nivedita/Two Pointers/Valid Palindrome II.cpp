class Solution {
public:
    bool palindrome(string s,int i,int j)
    {
       int l=i;
       int r =j;
        while(i<=j)
        {
            if(s[i]!=s[j])
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    bool validPalindrome(string s) {
       
		
        int i= 0, j = s.length()-1;
        while(i<=j)
        {
            if(s[i]!=s[j])
            {
                return palindrome(s,i+1,j)|| palindrome(s,i,j-1);
            }
            else
            {
                i++;
                j--;
            }
        }
        
      return true;  
     
    }
};
