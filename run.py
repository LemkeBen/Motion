from linearPlanning.trajectory import trajectory

if __name__ == "__main__":
    my_trajectory = trajectory(1.0, 51.0, 0.0, 0.0)
    dx = 0.0
    hz = 200
    for t in range (round(4.641 * hz)):
        v = my_trajectory.getVatT(t / hz)
        try:
            dx += v * 1 / hz
        except:
            print("error")
        print (v)
    print ("dx", dx)