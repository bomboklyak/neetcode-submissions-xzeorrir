class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        while True:
            f = 1
            for i in range(n-1):
                if position[i] > position[i+1]:
                    position[i], position[i+1] = position[i+1], position[i]
                    speed[i], speed[i+1] = speed[i+1], speed[i]
                    f = 0
            if f:
                break
        position = position[::-1]
        speed = speed[::-1]
        # print(position)
        # print(speed)
        time = [0]*n
        for i in range(n):
            time[i] = (target-position[i])/speed[i]
        # print(time)
        mt = time[0]
        c = 1
        for t in range(1, n):
            if time[t] > mt:
                c += 1
                mt = time[t]
        return c