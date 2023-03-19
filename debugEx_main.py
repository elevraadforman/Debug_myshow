import random

# import a function 'lowest_running_average' from folder 
# 'func_folder' and 'file debug_function.py'
from func_folder.debug_function import lowest_running_average
# from MyClass_folder.PrintInput_file import PrintInput
from MyClass_folder import PrintClass


def average(d,n):
    avg = d/n
    return avg

def running_average(perm):
    avgs = []
    total = 0
    for i, num in enumerate(perm):
        total += num
        current_avg = average(total, i+1)
        avgs.append(current_avg)
    return avgs

def highest_running_average(perm):
    averages = running_average(perm)
    return max(averages)

def generate_permeabilities(n):
    local_num = 12
    return random.sample(range(1,1000),n)
    local_num = 14
    

#if __name__== "__main__":

    #calling diffenert functions
perm = generate_permeabilities(13) #can jump into
print("Numbers: ", perm)
print("Running average:", running_average(perm))
print("Lowest average: ", lowest_running_average(perm))
print("Highest average: ", highest_running_average(perm))

#define object of class
input_printer = PrintClass(perm)
#calling function of the object
print("Print class output: ")
input_printer.print_input()

end = 50
    
