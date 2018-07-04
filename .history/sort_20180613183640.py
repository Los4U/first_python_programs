numbers = [int(x) for x in input('Input numbers to sort: ').split()]

print(x)

def sortNumbers(tab):
    iterations = 1
    N = len(tab)
    while iterations < N:
        j = 0
        while j <= N-2:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
            j = j+1
        iterations = iterations+1
    return tab

print("Sorted Numbers: ", sortNumbers(numbers))

