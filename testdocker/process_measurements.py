import pandas as pd
import math

def load_measurements(filename):
    table = pd.read_csv(filename)
    x = table['x'].tolist()
    theta = table['theta'].tolist()
    r = table['r'].tolist()

    measurements = []
    for i in range(len(x)):
        m = [x[i],theta[i],r[i]]
        measurements.append(m)
    return measurements

def m2p(x,theta,r):
    xr = r * math.cos(theta)
    yr = r * math.sin(theta)
    return [x+xr, yr] #return tuple

def measurements_to_points(measurements):
    points = []
    for m in measurements:
        p = m2p(m[0],m[1],m[2])
        points.append(p)
    return points

def export_points(points, filename):
    df = pd.DataFrame()
    df['x'] = [p[0] for p in points]
    df['y'] = [p[1] for p in points]
    df.to_csv(filename)

if __name__ == '__main__':
    measurements = load_measurements(filename = "measurements.csv")
    points = measurements_to_points(measurements)
    export_points(points, filename = "points.csv")
