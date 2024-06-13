import math
from vector import Vec3
from ray import Ray


def render(scene):
    '''
     Main render function that traverse through pixels and do ray marching and 
     returns pixel values as a list of RGB per pixel
    '''
    pixels = []

    for j in range(scene.camera.height):
        for i in range(scene.camera.width):
            print(f'{j} -> {i}')    # Pixel processing progress

            # Calculating ray direction
            y = (1 - 2 * (j + 0.5) / scene.camera.height) * math.tan(scene.camera.fov / 2)
            x = (2 * (i + 0.5) / scene.camera.width - 1) * math.tan(scene.camera.fov / 2) * scene.camera.aspect_ratio()
            ray = Ray(Vec3(0, 0, 0), Vec3(x, y, -1))

            color = Vec3(0.35, 0.35, 0.35)   # Default background color

            min_t = float('inf')

            # Checking for ray hit with geometries and find color for ray hit
            for sphere in scene.geometries:
                hit, t = sphere.intersect(ray)
                if hit and t < min_t:
                    min_t = t
                    point = ray.origin + ray.direction * t
                    normal = (point - sphere.center).normalize()
                    color = sphere.material.shade(point, normal, scene.lights, ray)

            # Remapping colour to 0-255
            r = min(int(color.x * 255), 255)
            g = min(int(color.y * 255), 255)
            b = min(int(color.z * 255), 255)
            pixels.append([r,g,b])

    return pixels