"""
File: class_reviews.py
Name:Angel Chen
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your program should be case-insensitive.
If the user input -1 for class name, your program would output
the maximum, minimum, and average among all the inputs.
"""


def main():
    t1 = 0
    t2 = 0
    max001 = 0
    min001 = 0
    sum001 = 0
    max101 = 0
    min101 = 0
    sum101 = 0
    while True:
        a = input("Which class? ")
        a = a.upper()
        if a == "SC001":
            s1 = int(input("Score:"))
            if t1 == 0:
                max001 = s1
                min001 = s1
                sum001 = s1
                t1 += 1
            else:
                if s1 >= max001:
                    max001 = s1
                    sum001 += s1
                    t1 += 1
                if s1 <= min001:
                    min001 = s1
                    sum001 += s1
                    t1 += 1
                if min001 < s1 < max001:
                    sum001 += s1
                    t1 += 1
        elif a == "SC101":
            s2 = int(input("Score: "))
            if t2 == 0:
                max101 = s2
                min101 = s2
                sum101 = s2
                t2 += 1
            else:
                if s2 >= max101:
                    max101 = s2
                    sum101 += s2
                    t2 += 1
                if s2 <= min101:
                    min101 = s2
                    sum101 += s2
                    t2 += 1
                if min101 < s2 < max101:
                    sum101 += s2
                    t2 += 1
        elif a == "-1":
            if t1 == 0 and t2 == 0:
                print("No class scores were entered")
                break
            else:
                print("============="+"SC001"+"=============")
                if t1 == 0:
                    print("No score for SC001")
                else:
                    print("Max (001): " + str(max001))
                    print("Min (001): " + str(min001))
                    print("Avg (001): " + str(float(sum001/t1)))
                print("=============" + "SC101" + "=============")
                if t2 == 0:
                    print("No score for SC101")
                else:
                    print("Max (101): " + str(max101))
                    print("Min (101): " + str(min101))
                    print("Avg (101): " + str(float(sum101/t2)))
                break


pass


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
