grains = 1
total = 0
for section in range(1,65):
    print('Veld', str(section).rjust(2), ':', grains)
    total = total + grains
    grains = grains*2
print('Totaal  :', total)