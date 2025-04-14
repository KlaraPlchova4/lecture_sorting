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
        seznam.sort()
    else:
        seznam.sort()
        seznam.reverse()
    return seznam

def bubble_sort(number_array):
    n = len(number_array)
    for i in range(n - 1):
        for num_inx in range(n - i - 1):
            if number_array[num_inx] > number_array[num_inx + 1]:
                number_array[num_inx], number_array[num_inx + 1] = number_array[num_inx + 1], number_array[num_inx]
    print(number_array)
    return number_array

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    print(array)
    return array

def main():
    data = read_data("numbers.csv")
    print(data)
    for ales in list(data.values()):
        selection_sort(ales, "ascending")
        print(ales)
    bubble_sort(data["series_1"])
    insertion_sort(data["series_1"])
    pass


if __name__ == '__main__':
    main()


# samostatný úkol 1
# def selection_sort(seznam):
#     seznam = seznam.sort()
#     return seznam