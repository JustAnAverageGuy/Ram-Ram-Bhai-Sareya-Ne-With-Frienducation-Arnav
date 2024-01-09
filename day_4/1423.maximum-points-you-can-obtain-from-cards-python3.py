# @leet start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        n                  = len(cardPoints)
        length_of_excluded = n-k
        
        total_sum          = sum(cardPoints)
        curr               = sum(cardPoints[:length_of_excluded]) # could have been done earlier,
                                                                  # but doesn't really matter
        min_exclude        = curr

        for i in range(0, k):
            curr += cardPoints[i+n-k] - cardPoints[i] # in the i-th iteration
                                                      # the first i+1 cards are considered
            min_exclude = min(curr, min_exclude)

        return (total_sum - min_exclude)

# @leet end
