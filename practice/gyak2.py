import random

random_num_list = list()
min_index = 0
max_index = 0

for i in range(0, 50):
    random_num_list.insert(i, random.randrange(0, 100))

for i in range(0, 50):
    if(random_num_list[i] < random_num_list[min_index]):
        min_index = i
    if(random_num_list[i] > random_num_list[max_index]):
        max_index = i

print("Min number: " + str(random_num_list[min_index]))
print("Max number: " + str(random_num_list[max_index]))