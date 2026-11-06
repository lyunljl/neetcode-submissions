class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
            stack = []
            for asteroid in asteroids:
                destroyed = False
                while not destroyed:
                    if stack:
                        if stack[-1] > 0 and asteroid < 0:
                            if abs(stack[-1]) > abs(asteroid):
                                destroyed = True
                            elif abs(stack[-1]) < abs(asteroid):
                                stack.pop()
                            else:
                                stack.pop()
                                destroyed = True
                        else:
                            stack.append(asteroid)
                            destroyed = True
                    else:
                        stack.append(asteroid)
                        destroyed = True
            return stack
