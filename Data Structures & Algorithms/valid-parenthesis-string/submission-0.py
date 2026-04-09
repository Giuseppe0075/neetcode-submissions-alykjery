class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        stars = []

        for i in range(len(s)):
            print(stack, stars)
            if s[i] == '(': #(
                stack.append(i)
            elif s[i] == ')':#)
                if stack:
                    stack.pop()
                elif stars and stars[-1] < i:
                    stars.pop()
                else:
                    return False
            else: #*
                stars.append(i)

        #For remaining ( and *
        while stack and stars:
            if stack[-1] > stars[-1]:
                return False
            stack.pop()
            stars.pop()
            
        return not stack


        # ((*)