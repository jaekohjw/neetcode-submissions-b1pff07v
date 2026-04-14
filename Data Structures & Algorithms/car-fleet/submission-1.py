class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        arr.sort(reverse=True)

        stack = []
        for car in arr:
            time = (target - car[0]) / car[1]
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)
