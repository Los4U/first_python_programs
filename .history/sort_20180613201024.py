import sys
def inputNumbers():
    test = True
    while test:
        try:
            numbers = [int(x) for x in input('Input numbers to sort: ').split()]  
            test = False
            return numbers  
        except ValueError: 
            print("Please enter ONLY a numbers separeted with space!")
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

def printNumbers(tab2):
    print("Numbers to sort:", tab2)
    print("Sorted Numbers: ", sortNumbers(tab2))

if len(sys.argv) > 1:
    words = []

    for i in sys.argv[1:]:
        #print("i = ", i)
        try:
            words.append(int(i))  #  [i] = int(sys.argv[int(i)])
        except ValueError: 
            print("Please enter ONLY a numbers separeted with space!")
            break
    printNumbers(words)
else:
    printNumbers(inputNumbers())


