# Numbers

# Integer
# Boolean
# Real
# Complex




black_tea_grams = 14
ginger_grams = 3

total_gram = black_tea_grams + ginger_grams
print(f"ginger_grams : {total_gram}")

remaining_tea = black_tea_grams - ginger_grams
print(f"remaining tea in gram : {remaining_tea}")

milk_liters = 7
serving = 4
milk_per_serving = milk_liters/serving
print(f"milk per serving is : {milk_per_serving}") # 1.75
print(f"milf per serving with no decimal : {milk_liters//serving}") # 1


'''
    / --> decimal
    // integer
    % modulo(remainder)
'''

num1 = 3;
num2 = 2;

print(f"num1 % num2 : {num1%num2}")


is_boiling = True
count = 5
total_actions = is_boiling + count # upcasting
print(f"total_actions : {total_actions}")

milk_present = 0;
print(f"milk present : {bool(milk_present)}") # automatically convert it into false

'''
None
0 
they are converted into false
'''

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print("can server" , can_serve);
