state_of_doors = ["closed"] * 100  #generate 100 closed door

#Change door state, Open the closed doors, and close the opened doors
def change_door_state(door_index):
    if (state_of_doors[door_index] == "closed"):
        state_of_doors[door_index] = "open"
    else:
        state_of_doors[door_index] = "closed"

#Change the doors state 100 times based on the rules.
for x in range(0, 100):
    for y in range(x, len(state_of_doors), x+1):
        change_door_state(y)
    
#Write out the numbers of opened doors
print("The following doors are open: ",end= "")
for y in range(0, len(state_of_doors)):
    if(state_of_doors[y] == "open"):
        print(str(y+1) + " ", end= "")

print() #Break the line for proper terminal layout