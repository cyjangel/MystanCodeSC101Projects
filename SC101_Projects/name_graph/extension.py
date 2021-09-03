"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        male_number = 0
        female_number = 0
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items1 = soup.find_all("td")   # 我們需要的資料在很多td裡面，所以先早到所有的td
        dict_content = []
        for item in items1:            # 將所有的td加到dict_content這個list中
            dict_content += item
        for i in range(len(dict_content)):              # 從i=0，到dict_content中的最後一筆都要判斷
            if i % 5 == 2:                              # 從規律發現每第2, 7, 9...筆資料都是男生名字使用的次數
                number1 = dict_content[i]
                number1 = number1.replace(",", "")      # 男生名字使用的次數中百位數和千位數之間有","，把他替換成""
                if number1.isdigit() and len(number1) > 4:
                    # 排除可能符合第2+5n筆中，但不是數字的資料，或者是數字但不是排名中的數字(排名中的數字都超過4位數)
                    # 若是男生的排名數字，要把他加起來
                    male_number += int(number1)
            elif i % 5 == 4:                             # 從規律發現每第4, 14, 19...筆資料都是女生名字使用的次數
                number2 = dict_content[i]
                number2 = number2.replace(",", "")
                if number2.isdigit() and len(number2) > 4:  # 女名字使用的次數中百位數和千位數之間有","，把他替換成""
                    # 排除可能符合第4+5n筆中，但不是數字的資料，或者是數字但不是排名中的數字(排名中的數字都超過4位數)
                    # 若是女生的排名數字，要把他加起來
                    female_number += int(number2)
        print('---------------------------')
        print(year)
        print("Male Number: "+str(male_number))
        print("Female Number: "+str(female_number))


if __name__ == '__main__':
    main()
