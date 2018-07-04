allGuests = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print('Total number of items : ' + str(item_total))

displayInventory(allGuests)

# Running result:
# Inventory:
# 1 rope
# 6 torch
# 42 gold coin
# 1 dagger
# 12 arrow
# Total number of items : 62