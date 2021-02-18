import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def f(step, step_range):
    '''the function f(x) = sqrt(x) + cos(x)
    returns f(x)'''
    data = []
    for step in step_range:
        y = m.sqrt(step) + m.cos(step)
        data.append(y)
    return data
    
def analytic_derivative_f(step, step_range):
    '''the analytic derivative of f(x) = f'(x) = 1/2*x^(-1/2) - sin(x)
    returns f'(x)'''
    data = []
    for step in step_range:
        if step==0:
            y = None
        else:
            first_term = 1/2 * step**(-1/2)
            second_term = -1 * m.sin(step)
            y = first_term + second_term
        data.append(y)
    return data
    
    
if __name__ == "__main__":
    coarse_step = 0.8
    coarse_step_range = np.arange(0, 4*m.pi, coarse_step)
    fine_step = 0.01
    fine_step_range = np.arange(0, 4*m.pi, fine_step)
    
    
    #calculate f(x) coarsely
    true_function_coarse = f(coarse_step, coarse_step_range)
    #calculate f(x) finely
    true_function_fine = f(fine_step, fine_step_range)
        
    #calculate analytic derivative coarsely
    true_analytic_derivative_coarse = analytic_derivative_f(coarse_step, coarse_step_range)
    #calculate analytic derivative finely
    true_analytic_derivative_fine = analytic_derivative_f(fine_step, fine_step_range)
    
    
    #calculate coarse interpolation
    sparse_function_linear_interpolation = interp1d(coarse_step_range, true_function_coarse)
    sparse_function_cubic_interpolation = interp1d(coarse_step_range, true_function_coarse, kind='cubic')
    
    
    #plot true function
    plt.plot(fine_step_range, true_function_fine,
             color='black')
    #plot analytic derivative
    plt.plot(fine_step_range, true_analytic_derivative_fine,
             color='black', linestyle='dashed')
    #plot interpolation
    #plt.plot(fine_step_range, sparse_function_cubic_interpolation(fine_step_range), color='magenta')
    
    plt.legend(['f(x)', "f'(x)"], loc='best')
    
    plt.show()

