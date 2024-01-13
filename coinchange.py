number = { 500:0,
          200:0,
          100:0,
          50:0,
          20:0,
          10:0,
          5:0,
          2:0,
          1:0}

def count(coins, n, sum):
          global number 
          for n in coins:
                    if sum==0:
                            break  
                    if sum>n:
                              while sum>=n:
                                        number[n] += 1
                                        sum -=n
          return number
'''if (sum == 0):
                     return 1
              elif (n <= 0):
                    return 0
              else:
                    return count(coins, n - 1, sum) + count(coins, n, sum - coins[n - 1])'''

coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
n = len(coins)


sum = int(input("Enter the sum you want to achieve: "))
if sum < 0:
          print("Invalid sum. Please enter a non-negative number.")
else:
          count(coins,n,sum)
          print(number)
    #print(f"The number of ways to make the sum {sum} using the given coins is:")
    #print(count(coins, n, sum))
