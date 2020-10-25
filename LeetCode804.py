'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/unique-morse-code-words/
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {}
        result = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alpha = list(string.ascii_lowercase)
        for i in range(len(alpha)):
            morse_dict[alpha[i]] = morse[i]
        for ele in words:
            temp = ""
            for alphabet in ele:
                temp = temp+morse_dict[alphabet]
            result.append(temp)
        set_result = set(result)
        return len(set_result)
