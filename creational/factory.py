
class ShapeInterface:
    """An interface only defines methods, not attributes."""
    def draw(self): pass

    
class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")


class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")

        
class ShapeFactory:
    """A Factory pattern defines an interface for creating an object, but defer object instantiation
    to run time
    """
    @staticmethod
    def getShape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0, 'Could not find shape ' + type

