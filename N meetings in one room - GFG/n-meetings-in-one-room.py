#User function Template for python3
class meeting:
    def __init__(self,start,end,pos):
        self.start = start
        self.end = end
        self.pos = pos
        
class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
        l = []
        
        for i in range(0,n):
            l.append(meeting(start[i],end[i],i))
        
        l.sort(key=lambda x:x.end)
        # return l
        ans = [l[0].pos]
        
        limit = l[0].end
        
        for i in range(1,n):
            if l[i].start >limit:
                ans.append(l[i].pos)
                limit = l[i].end
                
        return len(ans)
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends