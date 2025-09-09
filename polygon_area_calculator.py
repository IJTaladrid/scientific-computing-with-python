# This project uses object-oriented programming to create a Rectangle class and a
# Square class, where Square is a subclass of Rectangle.

# The Rectangle class with methods for area, perimeter, diagonal, and more.
class Rectangle:
    """
    Represents a rectangle with a given width and height.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.
        """
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        """
        Sets the width of the rectangle.
        """
        self.width = width

    def set_height(self, height):
        """
        Sets the height of the rectangle.
        """
        self.height = height

    def get_area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.width * self.height

    def get_perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """
        Calculates and returns the diagonal length of the rectangle.
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        """
        Returns a string representing the rectangle using '*' characters.
        If the width or height is greater than 50, it returns an error message.
        """
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        """
        Calculates how many times another shape (Rectangle or Square)
        could fit inside the current rectangle without rotation.
        """
        if isinstance(shape, (Rectangle, Square)):
            width_fit = self.width // shape.width
            height_fit = self.height // shape.height
            return width_fit * height_fit
        return 0

# The Square class, which is a subclass of Rectangle.
class Square(Rectangle):
    """
    Represents a square, a special type of rectangle where width and height are equal.
    """
    def __init__(self, side):
        # Call the parent class constructor with the side as both width and height.
        super().__init__(side, side)

    def __str__(self):
        """
        Returns a string representation of the Square object.
        """
        return f"Square(side={self.width})"

    def set_side(self, side):
        """
        Sets the side length of the square. This updates both width and height.
        """
        self.width = side
        self.height = side

    def set_width(self, width):
        """
        Overrides the parent method to ensure setting width also updates height.
        """
        self.set_side(width)

    def set_height(self, height):
        """
        Overrides the parent method to ensure setting height also updates width.
        """
        self.set_side(height)

# --- Example Usage ---

# Creating a Rectangle object
rect = Rectangle(10, 5)
print(f"Created a rectangle: {rect}")
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")
print(f"Diagonal: {rect.get_diagonal():.2f}")
print("\nPicture:")
print(rect.get_picture())

# Changing the dimensions
rect.set_width(12)
rect.set_height(4)
print(f"Updated rectangle: {rect}")
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")

# Creating a Square object
square = Square(6)
print(f"\nCreated a square: {square}")
print(f"Area: {square.get_area()}")
print(f"Perimeter: {square.get_perimeter()}")
print(f"Diagonal: {square.get_diagonal():.2f}")
print("\nPicture:")
print(square.get_picture())

# Demonstrating set_side
square.set_side(7)
print(f"Updated square using set_side: {square}")
print(f"Area: {square.get_area()}")
print(f"Perimeter: {square.get_perimeter()}")

# Using get_amount_inside
rect_inside = Rectangle(4, 2)
print(f"\nCreated a rectangle to fit inside: {rect_inside}")
print(f"Amount of {rect_inside} that fits inside {rect}: {rect.get_amount_inside(rect_inside)}")

square_inside = Square(2)
print(f"Created a square to fit inside: {square_inside}")
print(f"Amount of {square_inside} that fits inside {rect}: {rect.get_amount_inside(square_inside)}")