import math

class Ellipse:
    #constructor
    def __init__(self,  semi_major_axis, semi_minor_axis, center_x = 0, center_y = 0):
        self.center_x = center_x
        self.center_y = center_y
        self.semi_major_axis = semi_major_axis
        self.semi_minor_axis = semi_minor_axis

# get_center(self): Return a tuple containing the center coordinates.

# get_semi_major_axis(self): Return the length of the semi-major axis.

# get_semi_minor_axis(self): Return the length of the semi-minor axis.

# get_eccentricity(self): Return the eccentricity of the ellipse.

# get_foci(self): Return a tuple containing the coordinates of the foci.

# get_vertices(self): Return a tuple containing the coordinates of the vertices.

# get_area(self): Return the area of the ellipse.

# get_circumference(self): Return the circumference of the ellipse (approximation).

    def get_center(self):
        return (self.center_x, self.center_y)

    def get_semi_major_axis(self):
        return self.semi_major_axis

    def get_semi_minor_axis(self):
        return self.semi_minor_axis

    def get_eccentricity(self):
        e = math.sqrt(1 - (self.semi_minor_axis ** 2 / self.semi_major_axis ** 2))
        return e

    def get_foci(self):
        # (ae, 0) (-ae, 0)
        c = math.sqrt(self.semi_major_axis ** 2 - self.semi_minor_axis ** 2)
        foci_1 = (self.center_x - c, self.center_y)
        foci_2 = (self.center_x + c, self.center_y)
        return foci_1, foci_2

    def get_vertices(self):
        vertex_1 = (self.center_x - self.semi_major_axis, self.center_y)
        vertex_2 = (self.center_x + self.semi_major_axis, self.center_y)
        return vertex_1, vertex_2

    def get_area(self):
        area = math.pi * self.semi_major_axis * self.semi_minor_axis
        return area

    def get_circumference(self):
        h = ((self.semi_major_axis - self.semi_minor_axis) ** 2) / ((self.semi_major_axis + self.semi_minor_axis) ** 2)
        circumference = math.pi * (self.semi_major_axis + self.semi_minor_axis) * (1 + (3 * h / (10 + math.sqrt(4 - 3 * h))))
        return circumference
    
    #eqaution
    def generate_ellipse_equation(self):
        equation = f"((x - {self.center_x})/{self.semi_major_axis})^2 + ((y - {self.center_y})/{self.semi_minor_axis})^2 = 1"
        return equation
    
    def get_directrix_equation(self):
        e = math.sqrt(1 - (self.semi_minor_axis ** 2 / self.semi_major_axis ** 2)) 
        equation = f"x = {self.center_x} ± ({self.semi_major_axis} / {(e)})"
        return equation
    


    #distances between various entities, only couple of listed, many more to add..........
    def distance_foci(self):
        e = math.sqrt(1 - (self.semi_minor_axis ** 2 / self.semi_major_axis ** 2))
        return abs(2*self.semi_major_axis*e)
    
    def distance_directrixes(self):
        e = math.sqrt(1 - (self.semi_minor_axis ** 2 / self.semi_major_axis ** 2))
        return abs(2*self.semi_major_axis/e)
    








