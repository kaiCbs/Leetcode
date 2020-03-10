import random
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        a, b = random.random(), random.random()
        x = (a-0.5) * 2 * self.r  
        y = (b-0.5) * 2 * self.r  
        if  x**2 + y** 2 <= self.r **2:
            return [x+self.x, y+ self.y]
        return self.randPoint()
