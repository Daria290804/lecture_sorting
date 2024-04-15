import os
def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r", newline='\n') as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        iteration = 0
        for row in reader:
            for key, value in row.items():
                if iteration == 0:
                    data[key] =[int(value)]
                else:
                    data[key].append(int(value))
            iteration +=1
            return data

def selection_sort(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        min_index = i
        for j in range(i+1, len(list_of_numbers)):
            if list_of_numbers[j] < list_of_numbers[min_index]:
                min_index = j
        list_of_numbers[i], list_of_numbers[min_index] = list_of_numbers[min_index], list_of_numbers[i]
    return list_of_numbers

def main():
    numbers = [9, 2, 4523, 5, 4, 3, 4, 8, 11, 134541, 42]
    sorted_numbers = selection_sort(numbers)
    print("Sorted numbers:", sorted_numbers)

if __name__ == "__main__":
    main()

