class Lambert:
    def __init__(self, ka, kd):
        self.ka = kd
        self.kd = kd

    def shade(self, point, normal, lights, ray):
        '''
        Calculate just the diffuse
        '''
        color = self.ka
        for light in lights:
            light_direction = light.get_direction(point)
            diffuse = max(normal.dot(light_direction), 0) * self.kd
            color += diffuse * light.color
        return color

class Blinn:
    def __init__(self, ambient, diffuse, specular, spec_highlight):
        '''
        Calculate specular and reflection, needs more work here
        '''
        self.ka = ambient
        self.kd = diffuse
        self.specular = specular
        self.spec_highlight = spec_highlight

    def shade(self, point, normal, lights, ray):
        angle = ray.direction * -1
        color = self.ka
        for light in lights:
            light_direction = light.get_direction(point)
            diffuse = max(normal.dot(light_direction), 0) * self.kd
            reflection_direction = (2 * normal.dot(light_direction) * normal - light_direction).normalize()
            specular = max(angle.dot(reflection_direction), 0) ** self.spec_highlight * self.specular
            color += (diffuse + specular) * light.color
        return color

