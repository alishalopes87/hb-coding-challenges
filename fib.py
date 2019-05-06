# #Write a function that computes the list of the first 100 Fibonacci numbers. 
# By definition, the first two numbers in the Fibonacci sequence are 0 and 1, 
# and each subsequent number is the sum of the previous two. 
# example, here are the first 10 
#Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.

#iterate over range 1-100
#intialize empty list
#initlize current = lst[-2] + lst[-1]
#append current



def compute_fib():

	fib_nums = [0,1]

	for num in range(1,99):
		current_sum =fib_nums [-2] + fib_nums[-1]
		fib_nums.append(current_sum)

	return fib_nums

print(compute_fib())