from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                diff = abs(ast) - stack[-1]
                if not diff:
                    stack.pop()
                elif diff > 0:
                    stack.pop()
                    continue
                break
            else:
                stack.append(ast)

        return stack
            