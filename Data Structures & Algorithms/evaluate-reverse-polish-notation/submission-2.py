class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]

        for el in tokens:
            if el not in ops:
                stack.append(el)
            else:
                if el == "+":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    c = int(b)+int(a)
                    # print(f'{a}+{b}={c}')
                    stack.append(c)
                if el == "-":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    c = int(b)-int(a)
                    # print(f'{a}-{b}={c}')
                    stack.append(c)
                if el == "*":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    c = int(b)*int(a)
                    # print(f'{a}*{b}={c}')
                    stack.append(c)
                if el == "/":
                    a = stack.pop(-1)
                    b = stack.pop(-1)
                    c = int(b)/int(a)
                    # print(f'{a}/{b}={c}')
                    stack.append(c)

        return int(stack.pop())