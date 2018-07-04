import sys
def inputNumbers():
    test = True
    while test:
        try:
            numbers = [int(x) for x in input('Input numbers to sort: ').split()]  
            test = False
            return numbers  
        except ValueError: 
            print("Please enter a numbers separeted with space!")
            continue

def sortNumbers(tab):
    iterations = 1
    N = len(tab)
    while iterations < N:
        j = 0
        while j <= N-2:
            if tab[j] > tab[j+1]:
                temp = tab[j+1]
                tab[j+1] = tab[j]
                tab[j] = temp
            j = j+1
        iterations = iterations+1
    return tab

words = []
words = int(sys.argv[1:])

if len(words) > 1:
    print("Numbers to sort:", words)
    print("Sorted Numbers: ", sortNumbers(words))
else:
    nums = inputNumbers()
    print("Numbers to sort:", nums)
    print("Sorted Numbers: ", sortNumbers(nums))

