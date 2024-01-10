import numpy as np

def lcm_of_numbers(numbers):
    ans = np.lcm.reduce(numbers)
    return ans

x = input("Enter the numbers to find the LCM separated by spaces: ")
y = [int(num) for num in x.split()]
result = lcm_of_numbers(y)
print(result)
