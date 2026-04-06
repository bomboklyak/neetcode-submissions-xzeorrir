class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answer = [0]*n
        for i in range(n):
            while True:
                if not stack:
                    break
                posl = stack.pop(-1)
                if temperatures[i] > temperatures[posl]:
                    answer[posl] = i-posl
                else:
                    stack.append(posl)
                    break
            stack.append(i)
        return answer