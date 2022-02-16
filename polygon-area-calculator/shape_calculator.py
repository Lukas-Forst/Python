class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
    name = "Rectangle(width={}, height={})".format(self.width, self.height)
    return name
    
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2* self.width +2 * self.height
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if (self.width >= 50) or (self.height >= 50):
      return "Too big for picture."
    else:
      picture_string = ""
      for i in range(self.height):
        picture_string+=("{}\n".format("*"*self.width))
      return picture_string

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_amount_inside(self, shape1):
   
    Lo = self.width / shape1.width
    Wo = self.height / shape1.height
    no = Lo * Wo

    
    return int(no)

#Subclass of Rectangle
class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    name = "Square(side={})".format(self.width)
    return name

  def set_side(self, side):
    self.width = side
    self.height = side