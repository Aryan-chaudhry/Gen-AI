menu = ["simple dosa", "masala dosa", "paneer dosa", "simple utapam", "masala utapam", "paneer utapam"]



# without comprehension

# allDosa = []
# for item in menu:
#     if('dosa' in item):
#         allDosa.append(item)
# print(allDosa);


# with comprehension

# syntax [expression for item in iterable if condition]

allDosa = [item for item in menu if "dosa" in item] # make entire list in memmory

print(allDosa)



