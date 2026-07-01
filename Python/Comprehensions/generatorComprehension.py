#(expression fot item in iterable if condition) like a stream load one by one in memmory

daily_sales = [5,10,15,20,25]

# find any sale greater than 5 ruppes sum them out

totalSum = sum(sale for sale in daily_sales if sale > 5)

print(totalSum)