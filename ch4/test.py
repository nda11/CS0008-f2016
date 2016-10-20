n = 5
for i in range(n):
    for j in range(i):
        print ('* ')
        print('')

    for j in range(n, 0, -1):
        for i in range(j):
            print('* ')
            print('')