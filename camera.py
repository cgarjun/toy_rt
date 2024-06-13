class Camera:
    def __init__(self, width, height, fov):
        self.width =  width
        self.height =  height
        self.fov =  fov

    def aspect_ratio(self):
        return self.width / self.height