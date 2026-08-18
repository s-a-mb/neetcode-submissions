class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        # two stacks (one neg one pos)

        # negative

        # how to use a stack to evaluate both left and right


        collision = []
        broke = False

        for ast in asteroids:
            
            while collision and ast < 0 and collision[-1] > 0:
                if ast > 0 and collision[-1] > 0 or ast < 0 and collision[-1] < 0:
                    break
                elif abs(ast) > abs(collision[-1]):
                    collision.pop()
                elif abs(ast) == abs(collision[-1]):
                    broke = True
                    collision.pop()
                    break
                else:
                    broke = True
                    break
            
            if broke:
                broke = False
            else:
                collision.append(ast)

        return collision

