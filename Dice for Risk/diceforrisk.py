import random

att_num = list()
def_num = list()
attackers = 0
defenders = 0

while (attackers <= 0) | (attackers > 3):
    attackers = int(input("How many units attack: "))
while (defenders <= 0) | (defenders > 2):
    defenders = int(input("How many units defend: "))

for x in range(0, attackers):
    att_num.insert(x, random.randrange(1,7))
for x in range(0, defenders):
    def_num.insert(x, random.randrange(1,7))

print("Dice:")

text_nums = ' - '.join(str(e) for e in att_num)
print(" Attacker: " + text_nums)
text_nums = ' - '.join(str(e) for e in def_num)
print(" Defender: " + text_nums)


''' Old method, numbers without " - "
print(" Attacker: ", end="")
for x in range(0, attackers):
    att_num.insert(x, random.randrange(1,7))
    print(str(att_num[x]) + " ", end="")
print("\n")

print(" Defender: ", end="")
for x in range(0, defenders):
    def_num.insert(x, random.randrange(1,7))
    print(str(def_num[x]) + " ",  end="")
print("\n")
'''

att_num.sort(reverse=True)
def_num.sort(reverse=True)

att_lost_num = 0
def_lost_num = 0

if(len(att_num) > len(def_num)):
    for x in range(0, len(def_num)):
        if att_num[x] > def_num[x]:
            def_lost_num = def_lost_num + 1
        else:
            att_lost_num = att_lost_num + 1
else:
    for x in range(0, len(att_num)):
        if att_num[x] > def_num[x]:
            def_lost_num = def_lost_num + 1
        else:
            att_lost_num = att_lost_num + 1

print("Outcome: ")
print(" Attacker: Lost " + str(att_lost_num) + " units")
print(" Defender: Lost " + str(def_lost_num) + " units")