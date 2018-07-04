myPets = ['Zophie', 'Pooka', 'Fat=tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')

# Running result:
# Enter a pet name:
# Fod
# I do not have a pet named Fod

# Running result:
# Enter a pet name:
# Pooka
# Pooka is my pet.