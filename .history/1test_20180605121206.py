import sys
consonant = ["bcdfhhjklmnpqrstvqxz"]
vowel = ["aeiouy"] 

words = []
words = sys.argv
exception = ["be", "see", "flee", "knee", "etc" ]
for i in words:
    if i[-3] in consonant: #and i[-2] in vowel and i[-1] in consonant:
        i =  str(i + i[-1] + "ing")
        print(i)

    if  i.endswith("ie"):
        #i = i[:-2]   #].remove ie
        i =  str(i.replace("ie", "y")) + "ing"
        print(i)
    if  i.endswith("e") and not i in exception:
        i = i[:-1]   #].remove e
        i =  str(i) + "ing" #st[:-1]
        print(i)