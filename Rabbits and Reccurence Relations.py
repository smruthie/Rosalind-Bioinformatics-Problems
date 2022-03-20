#Fn = Fn-1 + Fn-2
rabbit_pairs = [1, 1]

n = 2
while True:
	onemonth_before = rabbit_pairs[n-1]
	twomonths_before = rabbit_pairs[n-2]
	Fn = onemonth_before + twomonths_before
	rabbit_pairs.append(Fn)
	n += 1
	if n == 49:
		break

print("The maximum you could enter is for 48 months!", "\n") # wanted to give the user an upper-limit of 3 years
months = int(input("Enter month for which you want to know how many rabbit pairs exist: "))
print("\n", "There are", rabbit_pairs[months], "rabbit pairs in", months, "months!")
