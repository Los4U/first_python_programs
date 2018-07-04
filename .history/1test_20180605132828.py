import sys
consonant = ["bcdfhhjklmnpqrstvqxz"]
vowel = ["aeiouy"] 

words = []
words = sys.argv
exception = ["be", "see", "flee", "knee", "etc" ]
for i in words:
    if i[-3] in consonant[0] and i[-2] in vowel[0] and i[-1] in consonant[0]:
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
    else:
        #print(str(i) + "ing")