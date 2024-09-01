
count = 0
with open("", "r") as file:
    for line in file:
        num_list = line.split()
        for num in num_list:
            count += num