"""
File: boggle.py
Name: Angel chen
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
python_lst = []   # 裝dictionary中的值


def main():
	start = time.time()
	lst = []
	sub_lst = []
	read_dictionary()
	for i in range(4):
		word = input(str(i+1) + " row of letters: ")
		if len(word) != 7:
			print("Illegal input")
			break
		for j in range(4):
			# 選取有字母的部分存入sub_lst
			sub_lst += word[j*2].lower()
		lst.append(sub_lst)
		sub_lst = []
	# print(lst)
	current_index_lst = []  # to store the current_index at (i, j)
	count = 0  # to store the total already found word
	for i in range(4):
		for j in range(4):
			# 可以讀到4*4中的所有字母(用座標的方式)
			letter = lst[i][j]
			# print(letter)
			current_index_lst.append((i, j))
			# print(current_index_lst)
			# 進入recursion，並獲得回傳值len(current_word_lst)
			a = find_all_the_letter(lst, i, j, letter, current_index_lst, [])
			count += a
			# print(current_index_lst)
			current_index_lst = []
	print("There are ", count, " words in total.")

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_all_the_letter(lst, i, j, letter, current_index_lst, current_word_lst):
	"""
	:param lst: the 4*4 characters which typed by the user.
	:param i: the order of row.
	:param j: the order of column.
	:param letter: the current letter which has been searching in the dictionary.
	:param current_index_lst: index which was already be searched.
	:param current_word_lst:  the letter which was already be found in the dictionary.
	:return: the len(current_word_lst) in the given i, j.
	"""
	global python_lst
	if letter in python_lst and len(letter) >= 4 and letter not in current_word_lst:
		print("Found \""+letter+"\"")
		current_word_lst.append(letter)
		# print("1")
	# 不可以加else，不然還沒搜尋完的字會提早在if結束，不會進到else(即尚未到達base case)
	# print("2")
	if has_prefix(letter) is True:
		for a in range(-1, 2):
			for b in range(-1, 2):
				# a 代表每個row中的i相鄰的字母 a為-1,0,1
				# b 代表每個column中的j相鄰的字母 b為-1, 0, 1
				if 0 <= a+i < 4 and 0 <= b+j < 4 and (a+i, b+j) not in current_index_lst:
					# 此邊界包含角落的字母只有3個相鄰、邊線上的字母有5個相鄰，中間的字母則有８個相鄰字母
					# 且不會存入已經已經讀過的index(a+i, b+j)
					# backtracking
					# choose
					letter += lst[a+i][b+j]
					current_index_lst.append((a+i, b+j))
					# explore
					find_all_the_letter(lst, a+i, b+j, letter, current_index_lst, current_word_lst)
					# un-choose:
					current_index_lst.pop()
					letter = letter[:-1]
	return len(current_word_lst)


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global python_lst
	with open(FILE, "r") as f:
		for line in f:
			python_lst += line.split()


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for current_word in python_lst:
		if current_word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
