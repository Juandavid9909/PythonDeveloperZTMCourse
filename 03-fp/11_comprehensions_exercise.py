some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

duplicates = set([x for x in some_list if some_list.count(x) > 1])

print(duplicates)