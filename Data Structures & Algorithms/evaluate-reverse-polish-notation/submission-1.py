class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el not in "+-*/":
                stack.append(int(el))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            if el == "+":
                stack.append(num1+num2)
            elif el == "-":
                stack.append(num1-num2)
            elif el == "*":
                stack.append(num1*num2)
            elif el == "/":
                stack.append(int(num1/num2))
                
        return stack.pop()