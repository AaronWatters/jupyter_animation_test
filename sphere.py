
from jp_doodle.nd_frame import swatch3d
import numpy as np

def sphere_point(theta, phi, radius=1.0):
    st = np.sin(theta)
    ct = np.cos(theta)
    sp = np.sin(phi)
    cp = np.cos(phi)
    return (radius * ct * cp, radius * sp, radius * st * cp)


def sphere(N, radius=1.0, color="rgba(100, 100, 200, 0.5)", color2="rgba(100,100,100,0.5)"):
    result = swatch3d()
    result.orbit_all(3)
    result.rotate_degrees((0,0,0), 3, (1, 1), 5)
    di = np.pi / N
    for i in range(2 * N):
        theta = di * i
        for j in range(N):
            c = color
            if (i + j) % 3 == 0:
                c = color2
            phi = di * (j - N * 0.5)
            triangle = [
                sphere_point(theta, phi, radius),
                sphere_point(theta + di, phi, radius),
                sphere_point(theta, phi + di, radius)
            ]
            result.polygon(triangle, c)
    return result
