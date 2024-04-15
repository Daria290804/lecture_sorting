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

def selection_sort(numbers, direction='ascending'):
    n = len(numbers)
    for i in range(n):
        if direction == 'ascending':
            min_idx = i
            for j in range(i+1, n):
                if numbers[j] < numbers[min_idx]:
                    min_idx = j
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
        elif direction == 'descending':
            max_idx = i
            for j in range(i+1, n):
                if numbers[j] > numbers[max_idx]:
                    max_idx = j
            numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]
        else:
            return None
    return numbers
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def main():
    numbers = [9, 2, 4523, 5, 4, 3, 4, 8, 11, 134541, 42]
    sorted_numbers = insertion_sort(numbers)
    print("Sorted numbers:", sorted_numbers)


if __name__ == "__main__":
    main()