"""
File: largest_digit.py
Name: Angel Chen
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the numbers which get from the main, and go to the helper function to find the largest digit.
	:return: the found largest digit to the main function.
	"""

	if n < 0:
		n = -1*n
	a = find_largest_digit_helper(n, 0)
	return a


def find_largest_digit_helper(n, current_largest_n):
	"""
	:param n: the numbers which get from the find_largest_digit function
	:param current_largest_n: the current largest digit of n
	:return: return the found largest digit to the find_largest_digit function
	"""
	if n < 1:
		# Base case
		pass
	else:
		compare = int(n) % 10
		if compare > current_largest_n:
			current_largest_n = compare
		# 	return find_largest_digit_helper(n/10, current_largest_n)
		# else:
		return find_largest_digit_helper(n/10, current_largest_n)
	return current_largest_n


if __name__ == '__main__':
	main()
