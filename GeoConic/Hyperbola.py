import numpy as np
import matplotlib.pyplot as plt


class Hyperbola:
    def __init__(self, a, b, h=0, k=0):
        self.a = a  # Semi-major axis
        self.b = b  # Semi-minor axis
        self.h = h  # x-coordinate of the center (default: 0)
        self.k = k  # y-coordinate of the center (default: 0)

    def get_focal_distance(self):
        # Focal distance (c) can be calculated using the formula: c = sqrt(a^2 + b^2)
        return (self.a**2 + self.b**2)**0.5

    def get_eccentricity(self): #yes
        # Eccentricity (e) can be calculated using the formula: e = c / a
        c = self.get_focal_distance()
        return c / self.a

    def get_vertex_distance(self):
        # Vertex distance (d) can be calculated using the formula: d = 2 * a
        return 2 * self.a

    def get_asymptote_equations(self):
        # Asymptote equations can be calculated as: y = +- (b / a) * (x - h) + k
        return f"y = {self.b / self.a} * (x - {self.h}) + {self.k}", f"y = {-self.b / self.a} * (x - {self.h}) + {self.k}"

    def get_standard_equation(self):
        # Standard equation of a hyperbola
        return f"((x - {self.h})^2 / {self.a**2}) - ((y - {self.k})^2 / {self.b**2}) = 1"

    def get_vertices(self):
        # Vertices are (±a + h, k)
        return (-self.a + self.h, self.k), (self.a + self.h, self.k)

    def get_directrix_equations(self):
        e = self.get_eccentricity()
        if self.a > self.b:
            # Horizontal hyperbola
            directrix_right = self.a / e + self.h
            directrix_left = -self.a / e + self.h
            return f"x = {directrix_right}", f"x = {directrix_left}"
        elif self.a < self.b:
            # Vertical hyperbola
            directrix_above = self.a / e + self.k
            directrix_below = -self.a / e + self.k
            return f"y = {directrix_above}", f"y = {directrix_below}"
        else:
            return "Invalid hyperbola (a cannot be equal to b)"
        
    def get_foci_points(self):
        # Foci points can be calculated as (±c, 0)
        c = self.get_focal_distance()
        # Foci points can be calculated as (±c + h, k)
        return (-c + self.h, self.k), (c + self.h, self.k)

    def get_latus_rectum_length(self):
        # Length of the latus rectum is 2b^2 / a
        return (2 * self.b**2) / self.a

    def get_latus_rectum_equation(self):
        # Equation of the latus rectum is x = ± a * e
        e = self.get_eccentricity()
        return f"x = {self.a * e}", f"x = {-self.a * e}"


    def get_latus_rectum_endpoints(self):
        # Endpoints of the latus rectum are (±ae, ±b^2 / a)
        e = self.get_eccentricity()
        endpoints = (
            (-self.a * e, self.b**2 / self.a),
            (-self.a * e, -self.b**2 / self.a),
            (self.a * e, self.b**2 / self.a),
            (self.a * e, -self.b**2 / self.a)
        )
        return endpoints

    def get_conjugate_hyperbola_equation(self):
        equation = f"((y - {self.k})^2 / {self.a**2}) - ((x - {self.h})^2 / {self.b**2}) = 1"
        return equation

    def get_auxiliary_circle_equation(self):
        radius = self.a
        equation = f"(x - {self.h})^2 + (y - {self.k})^2 = {radius**2}"
        return equation

    def point_position(self, x, y):
        equation_result = ((x - self.h)**2 / self.a**2) - ((y - self.k)**2 / self.b**2)

        if equation_result < 1:
            return "Inside"
        elif equation_result > 1:
            return "Outside"
        else:
            return "On"

    def get_director_circle_equation(self):
        c = (self.a**2 - self.b**2)
        equation = f"(x - {self.h})^2 + (y - {self.k})^2 = {c}"
        return equation
    def chord_equation(self, x1, y1, x2, y2):
        slope = (y2 - y1) / (x2 - x1)
        equation = f"y - {y1} = {slope} * (x - {x1})"
        return equation

    def tangent_equation(self, x1, y1):
        slope = self.b / self.a
        equation = f"y - {y1} = {slope} * (x - {x1})"
        return equation

    def normal_equation(self, x1, y1):
        slope = -self.a / self.b
        equation = f"y - {y1} = {slope} * (x - {x1})"
        return equation
    
    def plot(self):
        x = np.linspace(-10, 10, 400)  # Generate x values

        # Calculate y values based on the hyperbola equation
        y_pos = np.sqrt((self.b ** 2) * ((x ** 2) / (self.a ** 2) - 1))
        y_neg = -np.sqrt((self.b ** 2) * ((x ** 2) / (self.a ** 2) - 1))

        # Plot the positive branch of the hyperbola
        plt.plot(x, y_pos, label='Positive Branch')

        # Plot the negative branch of the hyperbola
        plt.plot(x, y_neg, label='Negative Branch')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Hyperbola')
        plt.legend()
        plt.grid(True)
        plt.axhline(0, color='black', linewidth=0.5)  # Add x-axis
        plt.axvline(0, color='black', linewidth=0.5)  # Add y-axis
        plt.show()
