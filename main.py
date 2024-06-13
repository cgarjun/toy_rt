from geom import Sphere
from vector import Vec3
from camera import Camera
from scene import Scene
from material import Lambert, Blinn
from light import Light
from render import render

def write_ppm(width, height, pixels, output):
    '''
    Quick utility function to write list of pixel data to ppm format
    '''
    ppm_header = f"P3\n{width} {height}\n255\n"
    with open(output, "w") as f:
        f.write(ppm_header)
        for i in pixels:
            f.write(f'{i[0]} {i[1]} {i[2]}\n')

def main(width, height, output='output.ppm'):
    '''
    Consider this function like a software like maya or houdini where 
    you build your scene, just that you are building in python
    '''
    red_material = Lambert(Vec3(0.3, 0, 0), Vec3(0.3, 0, 0))
    green_material = Blinn(Vec3(0, 0.3, 0), Vec3(0, 0.3, 0), Vec3(1, 1, 1), 32)
    blue_material = Blinn(Vec3(0, 0, 0.15), Vec3(0, 0, 0.15), Vec3(1, 1, 1), 32)

    cam = Camera(width, height, 1.2)

    scn = Scene(
            camera=cam,
            geometries = [
                Sphere(Vec3(0, 0, -5), 1, green_material),
                Sphere(Vec3(2, 0, -6), 1, red_material),
                Sphere(Vec3(-2, 0, -6), 1, blue_material)
            ],
            lights = [
                Light(Vec3(5, 10, 10), Vec3(0.3, 0.3, 0.3)),
                Light(Vec3(-5, -10, 10), Vec3(0.5, 0.5, 0.5))
            ]
        )

    pixels = render(scn)
    write_ppm(width, height, pixels, output)

if __name__ == '__main__':
    main(800, 600)