num_list = [4, 8, 42, 12, 99, 86, 2, 82]

greatest = 0
for num in num_list:
    if num > greatest:
        greatest = num

least = greatest
for num in num_list:
    if num < least:
        least = num
print(least)
