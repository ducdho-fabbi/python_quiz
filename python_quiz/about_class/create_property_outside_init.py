class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)

    @property
    def area(self):
        return self.height * self.width


def primary_school(height, width):
    return str(Rectangle(height, width))


print(primary_school(4, 8))
