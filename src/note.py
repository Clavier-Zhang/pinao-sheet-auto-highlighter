class Note:

    image = None

    top_left_point = None

    pos = None

    def __init__(self, image, top_left_point):
        self.image = image
        self.top_left_point = top_left_point