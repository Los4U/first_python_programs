import sys
from os import path
for arg in sys.argv:
    if len(sys.argv) == 2:
        if path.isfile(sys.argv[1]) and path.exists(sys.argv[1]):
            with open(sys.argv[1], 'r') as f:
                lines = f.read().splitlines()
                print(lines)
                i = 0
                j = 1 
                for i in range(0, len(lines)):
                    for j in range(j, len(lines)):
                        if sorted(lines[i]) == sorted(lines[j]):
                            print(str(i) + '. ' + str(lines[i])+ ' - ' + str(j) + '. ' +str(lines[j]))
                            j = j + 1
                i = i + 1
            f.close()
            break
        else:
            print("Input a correct name of a file.")
            break   
    elif len(sys.argv) == 1:
        print("Input file name right after program name to check the file for anagrams.")
        break
    else:
        print("You can input just one file!")
        break