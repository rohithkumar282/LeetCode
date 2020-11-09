'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/uncommon-words-from-two-sentences/
'''
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        sent1 = A.split(' ')
        sent2 = B.split(' ')
        result = []
        for ele in sent1:
            if ele not in sent2 and sent1.count(ele)==1:
                result.append(ele)
        for ele in sent2:
            if ele not in sent1 and sent2.count(ele)==1:
                result.append(ele)
        return result
