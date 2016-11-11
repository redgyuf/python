import csv
import os
#Step 1
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory=inv):
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

#Set arg to null if no argument given
def print_table(arg="null"):
    value_width = max([len(str(x)) for x in inv.values()])
    if value_width < 7:
        value_width = 7
    key_width = max(map(len, inv))
    if key_width < 13:
        key_width = 13

    print("Inventory:")
    print("{:>{v_width}} {:>{k_width}}".format("count", "item name", v_width = value_width, k_width = key_width))    
    print_line(key_width+value_width)
    
    if arg == "null":
        for key, value in inv.items():
            print("{:>{v_width}} {:>{k_width}}".format(value, key, v_width = value_width, k_width = key_width))

    elif arg == "count,asc":
        inv_list = sorted(inv.items(), key=lambda x:x[1])
        for key, value in inv_list:
            print("{:>{v_width}} {:>{k_width}}".format(value, key, v_width = value_width, k_width = key_width))

    elif arg == "count,desc":
        inv_list = sorted(inv.items(), key=lambda x:x[1], reverse=True)
        for key, value in inv_list:
            print("{:>{v_width}} {:>{k_width}}".format(value, key, v_width = value_width, k_width = key_width))
    else:
        print("Error: Wrong argument given to print_table() !!!")
    #print " - " based on key+value lengths
    print_line(key_width+value_width)
    print("Total number of items: " + str(sum(inv.values())))

print_table("count,des")

#Step 4
def import_inventory(filename="import_inventory.csv"):
    if os.path.isfile(filename):
        with open(filename) as csvfile:
            imported_dict = csv.DictReader(csvfile)
        for row in imported_dict:
            if(row["item_name"] in inv):
                inv.update({row["item_name"]: (int(inv.get(row["item_name"])) + int(row["count"]))})
            else:
                inv.update({row["item_name"]: int(row["count"])})
    else:
        print("Error: The file You want to import is not exist !!!")

import_inventory("sads")
display_inventory()