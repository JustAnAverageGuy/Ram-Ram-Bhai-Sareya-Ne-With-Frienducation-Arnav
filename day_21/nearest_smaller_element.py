# https://www.interviewbit.com/problems/nearest-smaller-element/
class Solution:
	# @param A : list of integers
	# @return a list of integers
    def prevSmaller(self, A):
        st = []
        ans = []
        for i in A:
            while st and (st[-1] >= i): st.pop()
            if not st: ans.append(-1)
            else: ans.append(st[-1])

            st.append(i)
        return ans
            
        
