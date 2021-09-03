"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any values.

    """
    if name not in name_data:
        # 如果名字還沒在dictionary中，便要把名字加入
        name_data[name] = {year: rank}
    else:
        if year not in name_data[name]:
            # 如果名字在不同年份有相對應的排名，要把新年份的排名加入
            name_data[name][year] = rank
        if year in name_data[name] and int(rank) < int(name_data[name][year]):
            # 如果新資料的名字在同年份已經出現過，如中性名字，應存入名次比較前面的排名
            # print(name_data[name])
            # print(name_data[name][year])
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.

    """
    with open(filename, "r") as f:
        start = 0
        for info in f:
            info_line = info.split(",")
            if start == 0:
                # 如果是每個檔案中的第一行，為年份
                year = info_line[0]
                year = year.strip()
                start += 1
            else:
                # 當start不再為0，即是第二行之後，文字順序分別為：排名、男生名、女生名，並把多餘的空格移除
                rank = info_line[0]
                rank = rank.strip()
                name_boy = info_line[1]
                name_boy = name_boy.strip()
                name_girl = info_line[2]
                name_girl = name_girl.strip()
                # 將year, rank, name利用add_data_for_name進行處理
                add_data_for_name(name_data, year, rank, name_boy)
                add_data_for_name(name_data, year, rank, name_girl)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for file in filenames:
        add_file(name_data, file)
    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string

    """
    names = []
    for name in name_data:
        check_name = ""
        for character in name:
            # 將在name_data中的每個name，以字母的方式，一個一個串到check_name中，並把它改成小寫(case-insensitive)
            check_name += character
            check_name = check_name.lower()
        if target.lower() in check_name:
            word = ""
            # 若小寫的target和check_name一樣，就把這個name用首字大寫其後小寫的方式，存入names中，最後return names
            word += check_name[0].upper()
            word += check_name[1:].lower()
            names += [word]
    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()
