
#get the input for user
number=input('give me the number:')

# assighn number
number=int(number)

# I test if it is out of range
if not(number>=0 and number<=36):
    print (' you enter number that outside the range')

if number==0:
    color='green'
    print ('your color is', color)
elif (number>=1 and number<=10) or (number >= 19 and number <= 28):
    if number %2==0:
        color=('black')
    else:
        color=('red')
    print ('your color is', color)
elif  (number>=11 and number<=18)or((number>=29 and number<=36)):
    if number %12==0:
        color=('red')
    else:
        color=('black')
    print ('your color is', color)