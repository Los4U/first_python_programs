i = 0
j = 1
k = 0
fib = 0
user_input = int(input("How many numbers print out? : "))
for fn in range(1,user_input+1):
    #if i < 30:
        print('{0:2d} {1:2s} {1:>30}'.format(fn,":", fib))
        #print(fib)
        fib = j+k
        j = k
        k = fib
    #else:
    #   print("3")
