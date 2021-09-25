class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffled = dict(zip(indices, s))
        answer = ""
        for i in range(len(indices)):
            answer += shuffled[i] 
        return answer
            
