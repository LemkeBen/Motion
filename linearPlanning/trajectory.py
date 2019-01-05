import math

"""
This is for trapezoidal or triangular acceleration.
Having differentstarting and ending velocities doesn't work.
"""

class trajectory:
    def __init__(self, x0, x1, v0, v1, maxAccel = 10,  maxVel = 17):
        self.x0 = x0
        self.x1 = x1
        self.v0 = v0
        self.v1 = v1
        self.maxAccel = maxAccel
        self.maxVel = maxVel
        self.generateTrajectory()

    def generateTrajectory(self):
        dx0to1 = self.x1 - self.x0

        dxatmaxTheoV = dx0to1 / 2
        self.maxTheoV = math.sqrt(self.v0 ** 2 + 2 * self.maxAccel * dxatmaxTheoV)

        self.cruiseV = min(self.maxVel, self.maxTheoV)
        self.dttomaxV = (self.cruiseV - self.v0) / self.maxAccel

        if self.maxVel < self.maxTheoV:  # trapezoidal
            dxtomaxV = (self.v0 + self.cruiseV) / 2 * self.dttomaxV
            dxatcruiseV = dx0to1 - dxtomaxV * 2
            dtatcruiseV = dxatcruiseV / self.cruiseV
            tAcandDc = 2 * self.dttomaxV
            self.dtTotal = dtatcruiseV + tAcandDc
        else:  # triangular
             self.dtTotal = 2 * self.dttomaxV

        print("dtTotal: ", self.dtTotal)

    def getVatT(self, t):
        if t > self.dtTotal:
            return "out of range"
        if self.maxTheoV <= self.maxVel:  # triangular
            if t <= self.dttomaxV:
                v = self.v0 + t * self.maxAccel
            else:
                v = self.cruiseV - (t - self.dttomaxV) * self.maxAccel
        else:  # trapezoidal
            if t <= self.dttomaxV:
                v = self.v0 + t * self.maxAccel
            elif t >= self.dtTotal - self.dttomaxV:
                v = self.v1 + (self.dtTotal - t) * self.maxAccel
            else:
                v = self.cruiseV
        return v