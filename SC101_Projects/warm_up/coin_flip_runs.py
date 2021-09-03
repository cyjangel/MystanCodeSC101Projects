"""
File: coin_flip_runs.py
Name: Angel Chen
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the runs!
"""

import random as r
name = ["H", "T"]


def main():
	t = 0
	l = ["a", "b", "c"]
	a = "@".join(l)
	print(a)
	# s = ""
	# for i in range(4):
	# 	roll = r.randint(1,6)
	# 	s += str(roll)
	# print(s)
	# n = 4
	# print("NUmber: "+str(n))
	# print("Number:", n)
	# print(f"Number: {n}")
	print("Let's flip a coin!")
	roll = ""
	roll2 = ""
	roll += r.choice(name)
	roll += r.choice(name)
	if roll[1] == roll[0]:
		t += 1
		roll2 += '1'
	else:
		roll2 += '0'

	num_run = int(input("Number of runs: "))
	i = 2
	while t < num_run:
		roll += r.choice(name)
		if roll[i] == roll[i-1]:
			roll2 += '1'
		else:
			roll2 += '0'

		if roll2[i-2] == '0' and roll2[i-1] == '1':
			t += 1
		i += 1
	print(roll)

	pass


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
