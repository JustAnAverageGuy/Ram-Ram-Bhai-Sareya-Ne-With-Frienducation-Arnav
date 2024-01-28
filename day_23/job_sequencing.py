#User function Template for python3


class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        optimal = sorted(Jobs, key=lambda x: -x.profit)
        slot = [False] * n
        count, profit = 0,0
        for i in optimal:
            for j in range(min(n, i.deadline)-1, -1, -1):
                if not slot[j]:
                    count += 1
                    profit += i.profit
                    slot[j] = True
                    break
        return count, profit


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha
class Job:
    '''
    Job class which stores profit and deadline.
    '''
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
    def __repr__(self) -> str:
        return str(self)
    def __str__(self):
        return f'({self.id}, {self.deadline}, {self.profit})'

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = Solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])
# } Driver Code Ends
