

def fact(n):
          if n==1 or n==1:
                    return 1
          else:
                    return n * fact(n-1)

def is_odd(n):
    return n % 2 == 1

def sum_odd_factorials(number):
    odd_factorial_sum = 0
    for i in range(1, number + 1):
        if is_odd(i):
            odd_factorial_sum += fact(i)
    return odd_factorial_sum

# Example usage:
x = int(input("Enter the number: "))
result = sum_odd_factorials(x)
print(f"The sum of odd factorials up to {x} is: {result}")
