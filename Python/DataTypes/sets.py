'''
    sets are mutable
    frozen sets are immutable
'''

numbers = {1,2,3,3,4,5} 
chars = {1,2,6,4,7}

union = numbers | chars # union

common = numbers & chars  # intersection
print(common)

differences = numbers - chars # difference
print(differences)