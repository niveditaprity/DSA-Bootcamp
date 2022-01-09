class Solution {
public:
    string removeDuplicates(string s) {
       stack<char>st;
        int i=0;
        int n=s.size();
        while(i<n)
        {
            if(!st.empty()&&st.top()==s[i])
            {
                st.pop();
            }
            else
            {
                st.push(s[i]);
            }
            i++;
        }
        string str;
        while(!st.empty())
        {
            str+=st.top();
            st.pop();
        }
      reverse(str.begin(), str.end());
 return str;
        
    }
};
