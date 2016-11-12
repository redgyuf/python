import csv
import os
#Set starting inventory and dragon loot
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#Displays the base inventory if no inventory(dictionary) given, else it displays the inventory(dict) it gets
def display_inventory(inventory=inv):
    print("Inventory:")    
    for key, value in inventory.items():
        print(value, key)
    print("Total number of items: " + str(sum(inventory.values())))

#Add items to a specific inventory(dictionary) from a list.
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inv:
            inventory[item] += 1
        else:
            inventory.update({item: 1})
    is_inventory_heavy()

#print line of "-", based on lenght(integer)
def print_line(lenght):
    for x in range(0, lenght+1):
        print("-", end="")
    print()

#Prints the content of the inventory in a table format and order the table based on argument(default: unordered)
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
        print("Print table failed!")
        print("Error: Wrong argument given to print_table() !!!")
    
    print_line(key_width+value_width)
    print("Total number of items: " + str(sum(inv.values())))

#Imports an inventory from a .csv file (default: "import_inventory.csv""), 
#if the file not exists or its extension is not proper, Error message will appear to user,
def import_inventory(filename="import_inventory.csv"):
    extension = os.path.splitext(filename)[1]
    if(extension == ".csv"):
        if (os.path.isfile(filename)):
            with open(filename) as csvfile:
                imported_dict = csv.DictReader(csvfile)
                for row in imported_dict:
                    if(row["item_name"] in inv):
                        inv.update({row["item_name"]: (int(inv.get(row["item_name"])) + int(row["count"]))})
                    else:
                        inv.update({row["item_name"]: int(row["count"])})
            print("Inventory import successfully finished.")
            is_inventory_heavy()
        else:
            print("Inventory import failed!")
            print("Error: The file You want to import is not exist !!!")
    else:
        print("Inventory import failed!")
        print("Error: The extension of the file You want to import is not proper (" + extension + "), please use .csv extension.")

#Export the inventory to a .csv file (default: "export_inventory.csv").
def export_inventory(filename="export_inventory.csv"):
    with open(filename, 'w') as csvfile:
        fieldnames = ['item_name', 'count']
        exported_dict = csv.DictWriter(csvfile, fieldnames=fieldnames)

        exported_dict.writeheader()
        for key, value in inv.items():
           exported_dict.writerow({"item_name": key, "count": value})
        print("Inventory export successfully finished to " + filename)

#Extra functions:
#Add one type of item to inventory (string,integer)
def add_item_to_inventory(item_name,count):
    inv.update({item_name: count})
    is_inventory_heavy()

#Remove one type of item. (string)
def remove_item_from_inventory(item_name):
    inv.pop(item_name)

#Remove all item from inventory.
def clear_inventory():
    inv.clear()

#Checks for flask and potion in inventory.
def ready_for_boss_kill():
    if("flask" in inv):
        print("You have " + str(inv.get("flask")) + " flask")
    else:
        print("You have no flask, buy one! because You have low DPS!")
    if("potion" in inv):
        print("You have " + str(inv.get("potion")) + " potion")
    else:
        print("You have no potion, buy one!")

#Check the amount of items in the inventory and Returns TRUE if its too heavy. 
#(True,False for further development)
def is_inventory_heavy():
    if(sum(inv.values()) > 100):
        print("Your inventory is too heavy, You will be slower!")
        return True
    else:
        return False