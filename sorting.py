import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

# samostatný úkol 1 a 2
def selection_sort(seznam, direction = "ascending"):
    if direction == "ascending":
        seznam = seznam.sort()
    else:
        seznam.sort()
        seznam.reverse()
    return seznam

def main():
    data = read_data("numbers.csv")
    print(data)
    for ales in list(data.values()):
        selection_sort(ales, "descending")
        print(ales)
    pass


if __name__ == '__main__':
    main()


# samostatný úkol 1
# def selection_sort(seznam):
#     seznam = seznam.sort()
#     return seznam