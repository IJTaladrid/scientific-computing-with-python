class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, shape):
        if isinstance(shape, (Rectangle, Square)):
            width_fit = self.width // shape.width
            height_fit = self.height // shape.height
            return width_fit * height_fit
        return 0

# The Square class, which is a subclass of Rectangle.
class Square(Rectangle):
    def __init__(self, side):
        # Call the parent class constructor with the side as both width and height.
        super().__init__(side, side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
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