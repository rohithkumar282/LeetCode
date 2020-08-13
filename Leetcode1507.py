'''
   Author: Rohith Kumar Punithavel
   Email: rohithkumar@asu.edu
   Problem Statement: https://leetcode.com/problems/reformat-date/
'''

class Solution:
    def reformatDate(self, date: str) -> str:
        month = {'Jan': '01', 'Feb' : '02', 'Mar': '03', 'Apr':'04', 'May':'05', 'Jun': '06', 'Jul': '07', 'Aug':'08', 'Sep': '09', 'Oct': '10', 'Nov':'11', 'Dec':'12'}
        remove_char = ['th','nd','rd','st']
        result=date.split(" ")
        for ele in remove_char:
            result[0]=result[0].replace(ele,'')

        if (int(result[0])<10):
            result[0]='0'+result[0]

        return (result[2]+'-'+month[result[1]]+'-'+result[0])
