import sys
exceptions = ['be', 'see', 'flee', 'knee', 'agree', 'go', 'do']
for arg in sys.argv[1:]:
    i = 0
    word = str(arg)
    if arg in exceptions:
        print(arg + 'ing')
    else:
        if len(str(arg)) < 4:
                if arg.endswith('g'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('p'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('r'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('d'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('b'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('l'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('t'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('n'):
                    print(arg + arg[-1] + 'ing')
                elif arg.endswith('ie'):
                    print(arg.replace('ie', 'ying'))
        else:
                if arg.endswith('ee'):
                    print(arg.replace('ee', 'ing'))
                elif arg.endswith('e'):
                    print(word[:-1] + 'ing')
                else:
                    print(arg + 'ing')