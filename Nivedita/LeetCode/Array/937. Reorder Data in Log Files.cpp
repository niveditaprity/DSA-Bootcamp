class Solution {
public:
 bool static my_compare(string a, string b)
{
   int i = a.find(" ")+1;
   int j = b.find(" ")+1;
   int c = (a.substr(i)).compare(b.substr(j));
    if (c == 0)
        return a.substr(0,i-1) < b.substr(0,j-1);
        else return (c<0); 
    
}
    vector<string> reorderLogFiles(vector<string>& logs) {
      vector<string>los;
        vector<string>digs;
        for(int i=0;i<logs.size();i++)
        {
            int j=logs[i].find(" ")+1;
            if(isdigit(logs[i][j]))
            {
                digs.push_back(logs[i]);
            }
            else
            {
                los.push_back(logs[i]);
            }
        }
        sort(los.begin(),los.end(),my_compare);
        vector<string>s;
        for(int i=0;i<los.size();i++)
        {
            s.push_back(los[i]);
        }
        for(int j=0;j<digs.size();j++)
        {
            s.push_back(digs[j]);
        }
        return s;
        
    }
};
