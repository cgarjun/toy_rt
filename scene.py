class Scene:
    '''
    Simple scene description as a python object
    '''
    def __init__(self,
                camera,
                geometries,
                lights,
                ) -> None:
        self.camera = camera
        self.geometries = geometries
        self.lights = lights