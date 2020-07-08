# Day 06 - Usage of lists

shoppingList = []
while True:     # add user input to a list
    print('For the grocery list, add the name of item ' + str(len(shoppingList) + 1) + '\n(or hit enter to stop)')
    name = input()
    if name == '':  # break loop if input is nothing
        break
    if name not in shoppingList:    # check for dublicate input (if input is already in list)
        shoppingList = shoppingList + [name]
    else:
        print(name + ' is already on the list.')

print('Grocery list contains:')
for name in shoppingList:   # print out each element of the list
    print(' ' + name)