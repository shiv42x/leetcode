class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) > abs(asteroid):
                    asteroid = 0
                    break
                else:
                    stack.pop()
                    asteroid = 0
                    break
            if asteroid: stack.append(asteroid)                
    
        return stack