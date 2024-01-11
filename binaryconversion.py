'''def decimal_to_binary(decimal_number):
              if decimal_number == 0:
                return "0"
              elif decimal_number == 1:
                return "1"
              else:
                return decimal_to_binary(decimal_number // 2) + str(decimal_number % 2)

num1 = int(input("Enter the number: "))
binary_representation = decimal_to_binary(num1)

print(f"The binary representation of {num1} is: {binary_representation}")'''


def decimaltobinary(n):
          if n != 0:
                    decimaltobinary(n//2)
          print(n%2 ,end="")
          
decimaltobinary(23)
