#Step 1
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")    
    for key, value in inventory.items():
        print(value, key)
    print("Total number of items: " + str(sum(inventory.values())))

#display_inventory(inv)

#Step 2
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inv:
            inventory[item] += 1
        else:
            inventory.update({item: 1})

add_to_inventory(inv, dragon_loot)
#display_inventory(inv)

#Step 3
def print_line(lenght):
    for x in range(0, lenght+1):
        print("-", end="")
    print()

def print_table():
    value_width = max([len(str(x)) for x in inv.values()])
    if value_width < 7:
        value_width = 7
    key_width = max(map(len, inv))
    if key_width < 13:
        key_width = 13

    print("Inventory:")

    print("{:>{v_width}} {:>{k_width}}".format("count", "item name", v_width = value_width, k_width = key_width))
    #print " - " based on key+value lengths
    print_line(key_width+value_width)
    #print out dictionary content
    for key, value in inv.items():
        print("{:>{v_width}} {:>{k_width}}".format(value, key, v_width = value_width, k_width = key_width))
    #print " - " based on key+value lengths
    print_line(key_width+value_width)
    print("Total number of items: " + str(sum(inv.values())))

print_table()