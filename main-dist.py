import matplotlib.pyplot as plt
import math
from NormalDist import NormalDistribution

class EmptyListInputError(Exception):
    pass

# try a test list
x = [5,0.34,7,45,21,2,13,15,56,59,78.5,4.6,27.3]
# x = []
nd_init = NormalDistribution(x,0.0,0.0)
ret_data = nd_init.read_data("body_fat.csv") # data.txt, body_fat.csv

try:
    if len(ret_data) == 0:
        raise EmptyListInputError(f"List {ret_data}, cannot be zero length or empty")
except EmptyListInputError as emptylist:
    print(f"The input disribution list can\'t be zero \n{emptylist}")
else:
    count, meanval = nd_init.get_mean(ret_data)
    print(f'debug...The number of items in the distribution is {count}')
    print(f'debug...The average of the distribution is {meanval}')
    
    my_variance = nd_init.get_variance(ret_data,meanval)
    print(f"Distribution variance is: {my_variance}")
    my_std_dev = math.sqrt(my_variance)
    print(f"Distribution standard deviation is: {my_std_dev}")
    
    nd1 = NormalDistribution(ret_data, meanval, my_std_dev)
    my_count, my_mean = nd1.get_mean(ret_data)
    
    print(f'The number of items in the distribution is {my_count}')
    print(f'The average of the distribution is {my_mean}')

    # now we try to compute the exponent term
    my_exp_list = nd1.exponent()
    print(f'The exponent list is: {my_exp_list}')

    # now trying to get the normal distribution
    my_nd_list = nd1.normal_dist()
    print(f'The normal distribution is: {my_nd_list}')
    
    # debugging the file reader
    # print(f"Size of data returned is: {len(my_data)}")
    # my_data_num = []
    # for i in range(len(my_data)):
    #     my_data_num.append(float(my_data[i]))

    # print(my_data)
finally:
    print("Plotting the results of the generated Normal distribution")
    plt.figure(1)
    plt.plot(ret_data)
    
    plt.figure(2)
    plt.plot(my_nd_list)
    
    plt.figure(3)
    plt.plot(ret_data,my_nd_list)
    
    plt.show()
