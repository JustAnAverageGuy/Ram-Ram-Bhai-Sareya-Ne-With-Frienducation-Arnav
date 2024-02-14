# @leet start
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        nodes = {*range(n)}
        cnt = 0
        for i in range(n):
            if i in nodes:
                cnt += 1
                stk = [i]
                while stk:
                    k = stk.pop()
                    if k not in nodes: continue
                    nodes.remove(k)
                    for neigh in range(n):
                        if isConnected[k][neigh] and neigh in nodes:
                            stk.append(neigh)

        return cnt

        
# @leet end
