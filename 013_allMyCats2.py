catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are: ')
for name in catNames:
    print(' ' + name)

# Running result:
# Enter the name of cat 1 (Or enter nothing to stop.):
# Devil
# Enter the name of cat 2 (Or enter nothing to stop.):
# Jinx
# Enter the name of cat 3 (Or enter nothing to stop.):
# is
# Enter the name of cat 4 (Or enter nothing to stop.):
# a
# Enter the name of cat 5 (Or enter nothing to stop.):
# handsome
# Enter the name of cat 6 (Or enter nothing to stop.):
# boy
# Enter the name of cat 7 (Or enter nothing to stop.):

# The cat names are:
#  Devil
#  Jinx
#  is
#  a
#  handsome
#  boy