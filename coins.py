def min_coins(coins,amount):
	cache = {}

	for num in range(0,amount +1):
		max_amount = amount + 1
		for i in range(len(coins)):
			if num - coins[i] < 0:
				# print(num)
				val = 0
			else:
				val = cache.get(num-coins[i], None)
		
			curr_min = min(val + 1, max_amount)

			if max_amount > curr_min:
				max_amount = curr_min

		cache[num] = max_amount 

	return cache[amount]

print(min_coins([1,2,5],11))
print(min_coins([186,419,83,408],6249))