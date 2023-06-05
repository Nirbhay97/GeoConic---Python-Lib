import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        # Calculate the area of the circle
        return math.pi * self.radius**2

    def circumference(self):
        # Calculate the circumference of the circle
        return 2 * math.pi * self.radius

    def diameter(self):
        # Calculate the diameter of the circle
        return 2 * self.radius

    def is_point_inside(self, x, y):
        # Check if a point (x, y) is inside the circle
        distance = math.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)
        return distance <= self.radius

    def is_fully_inside(self, other_circle):
        # Check if another circle is fully inside this circle
        distance_centers = math.sqrt((self.center_x - other_circle.center_x)**2 + (self.center_y - other_circle.center_y)**2)
        return distance_centers + other_circle.radius <= self.radius

    def is_intersecting(self, other_circle):
        # Check if another circle intersects with this circle
        distance_centers = math.sqrt((self.center_x - other_circle.center_x)**2 + (self.center_y - other_circle.center_y)**2)
        return distance_centers < self.radius + other_circle.radius

    def translate(self, x_offset, y_offset):
        # Translate the circle by the given offsets
        self.center_x += x_offset
        self.center_y += y_offset

    def scale(self, scale_factor):
        # Scale the circle by the given factor
        self.radius *= scale_factor

    def get_equation(self):
        # Fetch the equation of the circle
        equation = f"(x - {self.center_x})^2 + (y - {self.center_y})^2 = {self.radius**2}"
        return equation
    
    def get_tangent_equation(self, x, y):
        # Find the equation of the tangent line from a given point (x, y) to the circle

        # Check if the point is inside or on the circle
        distance = math.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)
        if distance <= self.radius:
            return "point is inside/on circle"

        dx = x - self.center_x
        dy = y - self.center_y

        if dx == 0:
            # Handle the case when the point is vertically aligned with the center of the circle
            return f"x = {x}"
        else:
            slope = -dx / dy
            intercept = y - slope * x
            return f"y = {slope}x + {intercept}"

    def get_tangent_length(self, x, y):
        # Find the length of the tangent line from a given point (x, y) to the circle

        # Check if the point is inside or on the circle
        distance = math.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)
        if distance <= self.radius:
            return 0

        dx = x - self.center_x
        dy = y - self.center_y
        distance = math.sqrt(dx**2 + dy**2)
        return distance - self.radius

    def col_point_circle(x1, y1, x2, y2, x3, y3):
        # Find the equation of a circle passing through three non-collinear points

        mid_x1 = (x1 + x2) / 2
        mid_y1 = (y1 + y2) / 2

        mid_x2 = (x2 + x3) / 2
        mid_y2 = (y2 + y3) / 2

        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y3 - y2) / (x3 - x2)

        if slope1 == slope2:
            return "points are colinear"

        center_x = (mid_y2 - mid_y1 + slope1 * mid_x1 - slope2 * mid_x2) / (slope1 - slope2)
        center_y = slope1 * (center_x - mid_x1) + mid_y1

        radius = math.sqrt((x1 - center_x)**2 + (y1 - center_y)**2)

        equation = f"(x - {center_x})^2 + (y - {center_y})^2 = {radius**2}"
        return equation

    def get_x_intercept(self):
        # Calculate the x-intercepts of the circle

        if self.radius == 0:
            return []

        delta = self.radius**2 - (self.center_y**2)
        if delta < 0:
            return []

        x1 = self.center_x - math.sqrt(delta)
        x2 = self.center_x + math.sqrt(delta)

        return [(x1, 0), (x2, 0)]

    def get_y_intercept(self):
        # Calculate the y-intercepts of the circle

        if self.radius == 0:
            return []

        delta = self.radius**2 - (self.center_x**2)
        if delta < 0:
            return []

        y1 = self.center_y - math.sqrt(delta)
        y2 = self.center_y + math.sqrt(delta)

        return [(0, y1), (0, y2)]

    def get_x_intercept_length(self):
        # Calculate the length of the x-intercepts

        x_intercepts = self.get_x_intercept()
        if not x_intercepts:
            return 0

        length = abs(x_intercepts[0][0] - x_intercepts[1][0])
        return length

    def get_y_intercept_length(self):
        # Calculate the length of the y-intercepts

        y_intercepts = self.get_y_intercept()
        if not y_intercepts:
            return 0

        length = abs(y_intercepts[0][1] - y_intercepts[1][1])
        return length

    def get_chord_of_contact_equation(self, external_point_x, external_point_y):
        # Calculate the equation of the chord of contact

        dx = external_point_x - self.center_x
        dy = external_point_y - self.center_y

        # Check if the external point lies on the circle
        if dx**2 + dy**2 <= self.radius**2:
            return "point lies on/inside the circle and the chord is undefined."

        # Calculate the slope of the tangent line
        slope = -dx / dy

        # Calculate the y-intercept of the tangent line
        y_intercept = external_point_y - slope * external_point_x

        return "y = {}x + {}".format(slope, y_intercept)

    def get_chord_of_contact_length(self, external_point_x, external_point_y):
        # Calculate the length of the chord of contact

        dx = external_point_x - self.center_x
        dy = external_point_y - self.center_y

        # Check if the external point lies on the circle
        if dx**2 + dy**2 <= self.radius**2:
            return "point lies on/inside the circle and the chord is undefined."


        # Calculate the distance between the points of contact
        distance = 2 * math.sqrt(dx**2 + dy**2 - self.radius**2)

        return distance
    
    def get_intersection_angle(self, other_circle):
        # Calculate the angle of intersection between two circles

        # Calculate the distance between the centers of the circles
        dx = other_circle.center_x - self.center_x
        dy = other_circle.center_y - self.center_y
        distance = math.sqrt(dx**2 + dy**2)

        # Check if the circles are separate or concentric
        if distance > self.radius + other_circle.radius:
            return None

        # Check if one circle is contained within the other
        if distance < abs(self.radius - other_circle.radius):
            return None

        # Check if the circles are identical
        if self.center_x == other_circle.center_x and self.center_y == other_circle.center_y and self.radius == other_circle.radius:
            return 2 * math.pi

        # Calculate the angle between the centers of the circles
        angle = math.atan2(dy, dx)

        # Calculate the angles at which the two circles intersect
        theta_1 = math.acos((self.radius**2 + distance**2 - other_circle.radius**2) / (2 * self.radius * distance))
        theta_2 = math.acos((other_circle.radius**2 + distance**2 - self.radius**2) / (2 * other_circle.radius * distance))

        # Calculate the total angle of intersection
        intersection_angle = theta_1 + theta_2

        return intersection_angle


    def __str__(self):
        return f"Circle with center ({self.center_x}, {self.center_y}) and radius {self.radius}"
    
    