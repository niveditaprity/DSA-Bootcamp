class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
      
        queue<int>q;
        int count0=0,count1=0;
        for(int i=0;i<students.size();i++)
        {
            q.push(students[i]);
          if(students[i]==0)
          {
              count0++;
          }
            else
            {
                count1++;
            }
        }
        int i=0;
       while(!q.empty())
       {
           int f=q.front();
           if(f==sandwiches[i])
           {
            q.pop();
               i++;
               
               f==1?count1--:count0--;
            }
           else
           {
             if(f==1&&q.size()==count1)
             {
                 break;
             }
               if(f==0&&q.size()==count0)
               {
                   break;
               }
               q.pop();
               q.push(f);
           }
           
       }
        return q.size();
        
    }
};
