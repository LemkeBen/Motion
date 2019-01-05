import math


class linear_trajectory:
    def __init__(self, x0, x1, v0, v1):
        self.x0 = x0
        self.x1 = x1
        self.v0 = v0
        self.v1 = v1
        # v1 ^ 2 = v0 ^ 2 + 2(a)(dt) (big four kinematic formulas)
        dx =  x1 - x0
        self.a = (v1 ** 2 - v0 ** 2) / (2 * dx)
        if (v0 != v1):
            dt = (v0 - v1) / self.a
        else:
            dt = dx / v0
    def getVatT(self, t):
        return t * self.a + self.v0
