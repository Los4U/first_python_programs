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

def inputNumbers():
    test = True
    while test:
        try:
            numbers = [int(x) for x in input('Input numbers to sort: ').split()]  
            test = False  
        except ValueError: 
            print("Please enter a numbers separeted with space!")
            continue

inputNumbers()
print("Numbers to sort:", numbers)
print("Sorted Numbers: ", sortNumbers(numbers))