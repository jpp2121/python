outF = open('Desktop/fall22/data/color_chart.txt', 'w')
inF = open('Desktop/fall22/data/input_stuff.txt', 'r')
# Read the data from the input file into the lists that I need
colors = []
items = []
# Use a dictionary to store the lists for each color
D = {}
# file reading loop
for line in inF:
    LL = line.strip().split('-')
    

    if LL[0] not in items:
        items.append(LL[0])

    if LL[1] not in colors:
        colors.append(LL[1])

    heldcolor = LL[1]

    if heldcolor in D.keys():
        D[heldcolor].append(LL[0])
    else:
        D[heldcolor] = [LL[0]]
l = -1

for c in colors:
    if len(c) > l:
        l = len(c)

l += 2
outF.write(" " * l)
# writing the items
for c in items:
    outF.write(c.center(len(c)+2))
outF.write('\n')
# write the colors
for i in colors:
    outF.write('-'*95+'\n')
    # creating the grid
    outF.write(i.rjust(l))
    for c in items:
        if c in D[i]:
            outF.write('x'.center(len(c) + 2))
        else:
            #if there isnt an x we still have to write a blank space and format it the same as an x
            outF.write('  '.center(len(c) + 2))

    outF.write('\n')
inF.close()
outF.close()
