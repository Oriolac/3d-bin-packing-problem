class Item:
    def __init__(self, name, length, width, height, weight):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.rotation = 0

    def get_volume(self) -> int:
        return self.length * self.height * self.width