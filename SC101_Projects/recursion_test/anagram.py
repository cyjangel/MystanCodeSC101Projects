"""
File: anagram.py
Name: Angel Chen
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_dict = []                # A list to store all the words in the FILE to become a dictionary.


def main():
    """
    :return: let user type a word and find all the anagram in the FILE, and if user types EXIT, stop the function.
    """
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    read_dictionary()
    while True:
        s = input("find anagram for: ")
        if s == EXIT:
            break
        else:
            find_anagrams(s)

    start = time.time()
    ####################
    #                  #
    #       TODO:      #
    #                  #
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    """
    :return: read the dictionary, and store in a list, which is called word_dict.
    """
    # word_dict裡面存有dictionary檔案中所有的單字
    global word_dict
    with open(FILE, "r") as f:
        for line in f:
            word_dict += line.split()


def find_anagrams(s):
    """
    :param s: the user type on the main function and call the find_anagrams_helper function.
    :return: print the number of anagrams and print all the anagrams in the FILE.
    """
    a = find_anagrams_helper(s, "", len(s), [], [])
    print(len(a), "anagrams:", a)


def find_anagrams_helper(s, current_word, ans_s, current_word_lst, current_index):
    """
    :param s: the word which typed on the main function.
    :param current_word: current word which is being searched in the dictionary(FILE).
    :param ans_s: the target length of the current word equals to the original s.
    :param current_word_lst: the current word which was already found in the dictionary and stored in the list.
    :param current_index: the current index of s, which is being searched.
    :return: return the current_word_list to the find_anagrams function.
    """
    if len(current_word) == ans_s:
        # Base case:
        if current_word in word_dict and current_word not in current_word_lst:
            current_word_lst.append(current_word)
            print("Searching...")
            print("Found: ", current_word)
    else:
        for i in range(len(s)):
            if str(i) in current_index:
                pass
            else:
                # Backtracking
                # choose
                current_index.append(str(i))
                current_word += s[i]
                # explore
                if has_prefix(current_word):
                    find_anagrams_helper(s, current_word, ans_s, current_word_lst, current_index)
                # un-choose
                current_word = current_word[:-1]
                current_index.pop()
    return current_word_lst


def has_prefix(sub_s):
    """
    :param sub_s: check the current word which is start with the capital sub_s is in the dictionary or not.
    :return: if the current word which is start with the capital sub_s, return True.
    """
    for current_word in word_dict:
        if current_word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
