my_file = (open("testfile.txt", mode='r'))

for line in my_file:
    print(line.strip())

my_file.close()

my_list = []
my_list.append("elso")
my_list.append("masodik")
my_list.append("harmadik")

my_file = (open("testfile.txt", mode='w'))

for i in my_list:
    my_file.write(i + "\n")
my_file.write("almafa")