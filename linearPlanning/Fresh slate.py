# same starting and ending velocity
import math

x0 = 0.0
x1 = 50
v0 = 0
v1 = v0

def trapezoidalTradgectory(x0, x1, v0, v1):
    maxAccel = 10  # ft/s^2
    maxVel = 17  # ft/s

    dx0to1 = x1 - x0

    dxatmaxTheoV = dx0to1 / 2
    maxTheoV = math.sqrt(v0 ** 2 + 2 * maxAccel * dxatmaxTheoV)

    cruiseV = min(maxVel, maxTheoV)
    dttomaxV = (cruiseV - v0) / maxAccel

    if maxVel < maxTheoV:  # trapezoidal
        dxtomaxV = (v0 + cruiseV) / 2 * dttomaxV
        dxatcruiseV = dx0to1 - dxtomaxV * 2
        dtatcruiseV = dxatcruiseV / cruiseV
        tAcandDc = 2 * dttomaxV
        dtTotal = dtatcruiseV + tAcandDc
    else:  # triangular
        pass

def getVatT(t):
    if maxTheoV <= maxVel: #triangular
        if t <= dttomaxV:
            v = v0 + t * maxAccel
        else:
            v = cruiseV - (t - dttomaxV) * maxAccel
    else: #trapezoidal
        if t<= dttomaxV:
            v = v0 + t * maxAccel
        elif t >= dtTotal - dttomaxV:
            v = v1 + (dtTotal - t) * maxAccel
        else:
            v = cruiseV
    return v

