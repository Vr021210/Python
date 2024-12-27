def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

number = []
numbers = []

AT = int(input("how many numbers u want to sort? "))


for i in range (AT):
    number = input(f"Tall {i+1}: ") 
    numbers.append(number)
insertion_sort(numbers)


print(numbers)