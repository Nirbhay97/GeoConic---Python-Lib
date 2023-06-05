import matplotlib.pyplot as plt
import numpy as np

def plot_tanget(*args, **kwargs):
    center_x, center_y, semi_major_axis, semi_minor_axis = args
    if 'x' in kwargs:
        x = kwargs['x']
    
    if 'y' in kwargs:
        y = kwargs['y']
    
    m = -(semi_minor_axis**2)*(x)/y
    c = semi_minor_axis**2/y
    x = np.linspace(-10, 10, 100)
    y = m * x + c
    plt.plot(x, y, label=f"y = {m}x + c") 


        
def plot_ellipse(*args, **kwargs):
    center_x, center_y, semi_major_axis, semi_minor_axis = args
    
    fig, ax = plt.subplots()

    angles = np.linspace(0, 2 * np.pi, 100)

    x = center_x + semi_major_axis * np.cos(angles)
    y = center_y + semi_minor_axis * np.sin(angles)

    # Plot the ellipse
    
    ax.plot(x, y, label='Ellipse')
    

    #tag
    if 'x' in kwargs:
        x = kwargs['x']
    
    if 'y' in kwargs:
        y = kwargs['y']
    
    m = -(semi_minor_axis**2)*(x)/y
    c = semi_minor_axis**2/y
    x = np.linspace(-5, 5, 100)
    y = m * x + c
    plt.plot(x, y, label=f"y = {m}x + c") 
    
    
    ax.set_aspect('equal')
    ax.legend()
    plt.show()

# plot_ellipse(0, 0, 5, 3)





