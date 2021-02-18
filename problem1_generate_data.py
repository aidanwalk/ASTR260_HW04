import numpy as np
import math

class Charge:
    """a charge object defined by its position and
    charge"""
    def __init__(self, xpos=None, ypos=None,
                 charge=None):
        self.xpos = xpos
        self.ypos = ypos
        self.charge = charge

class Potential:
    """a potential object defined by a list of charges"""
    def __init__(self, charges=None, #<--list_of_charge_objects,
                 x_values=None, y_values=None):
        self.charge_list = list_of_charge_objects
        self.x_values = x_values
        self.y_values = y_values
        self.potential = self.calculate_total_potential(self.charge_list)

    def calculate_total_potential(self, argument): #computer says: "calculate_total_potential() takes 1 positional argument but 2 were given>"
        '''calculates the total potential for each charge
        outputs a list of arrays of each potential'''
        potential = []
        total_potential = []
        enaught = 8.85418782e-12
        for charge in self.charge_list:
            charge_xpos = charge.xpos
            charge_ypos = charge.ypos
            
            #calculate distance from charge for all arrary data points
            y_distance_to_charge = charge_ypos - self.y_values
            x_distance_to_charge = charge_xpos - self.x_values
            distance_to_charge = ( y_distance_to_charge**2 + x_distance_to_charge**2 )**(1/2)
            
            #Calculate potential at each array point
            potential = charge.charge / (4*math.pi*enaught*distance_to_charge)
            #append potential array to total_potential list
            total_potential.append(potential)
        return total_potential

class Electric_field:
    """an electric field object defined by a potential"""
    def __init__(self, potential=None):
        self.potential = potential
        #central difference method
        h = 1
        #df/dx
        self.dx = self.dx_derivative(self.potential)
        #df/dy
        self.dy = self.dy_derivative(self.potential)
        
    def dx_derivative(self, argument2):
        dx_data = []
        for deriv_x in range(1, len(self.potential)-1):
            dx_cntl_diff = ( self.potential[deriv_x+1, :] - 
                             self.potential[deriv_x-1, :] ) /2
            dx_data.append(dx_cntl_diff)
        return dx_data
        
    def dy_derivative(self, argument3):
        dy_data = []
        for deriv_y in range(1, len(self.potential)-1):
            dy_cntl_diff = ( self.potential[:, deriv_y+1] -
                             self.potential[:, deriv_y-1] ) /2
            dy_data.append(dy_cntl_diff)
        return dy_data
   
if __name__ == "__main__":
    #define charges
    Charge1 = Charge(xpos=-0.05, ypos=0, charge=1)
    Charge2 = Charge(xpos=0.05, ypos=0, charge=1)
    list_of_charge_objects = [Charge1, Charge2]
    #generate x,y values
    spacing = 0.01 #<--spacing 0.01 m = 1 cm
    x_range = np.arange(-0.5, 0.5+spacing, spacing)
    y_range = np.arange(-0.5, 0.5+spacing, spacing)
    xs, ys  = np.meshgrid(x_range, y_range)

    #generate a list of arrays containing the potential of each charge at every point in arrary
    print('\nCalculating data for part A\n... ')
    data = Potential(charges=list_of_charge_objects, \
                     x_values=xs, \
                     y_values=ys)   
    
    #add both arrays in this list to find combined_potential on this sheet
    combined_potential = data.potential[0] + data.potential[1]
    
    #save part A data to .txt file for plotting
    fname_partA = 'calculated_potential.txt'
    np.savetxt(fname_partA, 
               combined_potential,
               delimiter=',',
               header='combined_potential, row=x, cols = y')
    print('Part A data saved to: ', fname_partA)
    
    print('\n\nCalculating data for part B:\n...')
    #calculate derivative
    derivative = Electric_field(potential=combined_potential)
    #Print partial derivatives at (0,0) and (0.05,0.07)
    print('At (0,0): ',
           '\n\tdf/dx = ', derivative.dx[0][0],
           '\n\tdf/dy = ', derivative.dy[0][0])
    print('At (0.05,0.07): ',
           '\n\tdf/dx = ', derivative.dx[5][7],
           '\n\tdf/dy = ', derivative.dy[5][7])
    print('Saving derivative data.\n...')
    #save text for plotting in part B
    fname_partB_dx_data = 'dx_potential_data.txt'
    fname_partB_dy_data = 'dy_potential_data.txt'
    np.savetxt(fname_partB_dx_data,
               derivative.dx, 
               delimiter=',',
               header='df/dx of potential data, row=x, cols=y',
               fmt = '%.5e')
    np.savetxt(fname_partB_dy_data,
               derivative.dy, 
               delimiter=',',
               header='df/dy of potential data, row=x, cols=y',
               fmt = '%.5e')
    print('Part B data saved to: ', fname_partB_dx_data, ' & ', fname_partB_dy_data)
