'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def combination(op_comb,num_guide,ele):
            list1=[]
            for op in op_comb:
                for var in num_guide[ele]:
                    list1.append(op+var)
            return list1

        output_comb=['']
        num_guide={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        if digits=="":
            output_comb=[]
        else:
            for ele in digits:
                output_comb=combination(output_comb,num_guide,ele)
        return output_comb
