
for i in range(0, 7):
    import random
lotterynumbers = []
x = 0

while x < 7:
    lotterynumbers.append(random.randint(0, 9))
    x += 1
print (lotterynumbers)