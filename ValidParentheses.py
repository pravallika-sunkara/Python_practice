'''
Given the input of parenthesis, we retrun if it is valid or not
Time: O(n)

'''

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {'{':'}','[':']','(':')'}
        stack = []
        print('Input String: ',s)
        for bracket in s:
            if bracket in bracket_map:
                stack.append(bracket_map[bracket])
            elif not stack or bracket != stack.pop():
                return False
        return not stack
    
if __name__ == "__main__":
    print(Solution().isValid("()"))
    print(Solution().isValid("()[{]}"))
