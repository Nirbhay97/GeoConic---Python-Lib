import math


class Parabola:
    #constructor
    def __init__(self,coeff_a, coeff_b, coeff_c):
        self.coeff_a=coeff_a
        self.coeff_b=coeff_b
        self.coeff_c=coeff_c


# get_verticx(self): Return a tuple containing the coordinates of the vertex.

# get_focus(self): Return a tuple containing the coordinates of the focus.

# get_eccentricity(self): Return the eccentricity of the parabola.

# get_focal_length(): returns the length of latus recturm

# get_latus_rectum(self): Returns length of latus rectum

    def get_vertex(self):
         h=-1*(self.coeff_b)/(2*self.coeff_a)
         k=((self.coeff_b*self.coeff_b)-(4*self.coeff_a*self.coeff_c))/(4*self.coeff_a)
         return (h, k)

    def get_focus(self):
        h=-1*(self.coeff_b)/(2*self.coeff_a)
        k=((self.coeff_b*self.coeff_b)-(4*self.coeff_a*self.coeff_c))/(4*self.coeff_a)
        p=1/(4*self.coeff_a) 
        return (h,k+p)

    def get_focal_length(self):
         return 1/(4*self.coeff_a)

    def get_eccentricity(self):
         e =1
         return e

    def get_latus_recturm(self):
        h=-1*(self.coeff_b)/(2*self.coeff_a)
        k=((self.coeff_b*self.coeff_b)-(4*self.coeff_a*self.coeff_c))/(4*self.coeff_a)  
        latus_rectum = 2*((self.coeff_a*h*h+self.coeff_b*h+self.coeff_c)-(k))
        return latus_rectum
    
    # get_parabola_equation(self): return the equation of parabola

    def get_parabola_equation(self):
        return f"y = {self.coeff_a}x^2 + {self.coeff_b}x + {self.coeff_c}"
    
    # get_assymptote_equation(self):Give the equation of Assymptote
    
    def get_assymptote_equation(self):
        if (self.coeff_b!=0):
          return f"y = {self.coeff_a/self.coeff_b}x"  
    
    # get_solpe_equation(self):gives equation of slope

    def get_slope_equation(self):
        if(self.coeff_b!=0):  
          return f"m = {2*self.coeff_a}x + {self.coeff_b}"
        else:
          return f"m = {2*self.coeff_a}x"

    




    





