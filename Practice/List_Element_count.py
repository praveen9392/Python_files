# from collections import Counter
# my_list = [1, 2, 3, 3, 4, 4, 4]
# counts = Counter(my_list)
# print(counts)

my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
counts = {}
for element in my_list:
    counts[element] = my_list.count(element)
print(counts)  # {1: 1, 2: 2, 3: 3, 4: 4}