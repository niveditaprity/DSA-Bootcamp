    def JobScheduling(self,jobs,n):
        srtjob = sorted(jobs,key = lambda job : job.profit,reverse=True)
        # code here
        
        maxi = max(job.deadline for job in srtjob)
                
        sched = [-1]*maxi
        
        profit = 0
        jobcount = 0
        
        for job in srtjob:
            n = job.deadline
            while n > 0:
                ind=n-1
                if sched[ind] == -1:
                    sched[ind] = job.id
                    profit += job.profit
                    jobcount += 1
                    profit
                    break
                n-=1
                
        return [jobcount,profit]
