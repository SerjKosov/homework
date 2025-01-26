# Задание 1
#print("Задание 1")
# a = True
# b = False
# c = False
# total = a or b #T или F (или) дает Т
# total_1 = a and b # Т и F (и) дает F
# total_2 = b or c #F или F точно F
# print(total, total_1, total_2)

# Задание 2
#print("Задание 2")
# a = True
# b = False
# c = False
# total = not a and b #(not a = F) and F = F
# total_1 = a or not b # T or (not F = T) = T
# total_2 = a and b or c # (T and F = F) and F = F
# print(total, total_1, total_2)

# Задание 3
#print("Задание 3")
# a = True
# b = False
# c = False
# total = a or b and not c #(a and b)= T, not c = T, T and T = T
# total_1 = a and not b or c # (T and (not F = T)) = T, T or F = T
# total_2 = not a and not b # (not T = F) and (not F = T) = F
# total_3 = a and (not b or c) # T and ((not F = T) or F = T) = T
# total_4 = not (a and c) or b # not (T and F = F) = T or F = T
# total_5 = a or(not (b and c)) # T or (любое значение, будет Т, но распишу) (not (F and F = F) = T) = T
# print(total, total_1, total_2, total_3, total_4, total_5)

#Задание 4
#print("Задание 4")
# x = True
# y = False
# z = False
# total = x or y and not z # (T or F = T) and (not F = T) = T
# total_1 = x and not y or z # (T and (not F = T)) = T or F = T
# total_2 = not x and not y # (not T = F) and (not F = T) = F
# total_3 = x and (not y or z) #T and ((not F = T) or F = T) = T
# total_4 = not(x and z) or y # (not(T and F = F) = T) or F = T
# total_5 = x or (not (y or z)) # T or (not (F or F = F) = T) = T
# print(total, total_1, total_2, total_3, total_4, total_5)

#Задание 5
#print("Задание 5")
# a = True
# b = False
# c = False
# total = a or not (a and b) or c # T or (not(T and F = F) = T) = T
# total_1 = not a or a and (b or c) # ((not T = F) or T = T) and (F and F = F) = F
# total_2 = (a or b and not c) and c # ((T or F = T) and (not F = T) = T) and F = F
# print(total, total_1, total_2)

#Задание 6
#print("Задание 6")
# a = True
# b = False
# c = False
# total = (not a or not b) and not c # ((not T = F) or (not F = T) = T) and (not F = T) = T
# total_1 = (not a or not b) and (a or b) #((not T = F) or (not F = T) = T and (T or F = T) = T
# total_2 = a and b or a and c or not c # ((T and F = F) or (T and F = F)) = F or (not F = T) = T
# print(total, total_1, total_2)

#Задание 8
# print("Задание 8")
# a, b, c = True, True, True
# total = not (a or not b and c) #not (T or ((not T =F) and T = F) =T) = F
# total_1 = a and not (b and not c) # T and (not(T and (not T = F) = F) = T) = T
# total_2 = not (not a or b and c) # not ((not T = F) or (T and T = T) = T) =F
# print(total, total_1, total_2)

# a, b, c = False, True, True
# total = not (a or not b and c) #not (F or ((not T =F) and T = F) =F) = T
# total_1 = a and not (b and not c) # F and (not(T and (not T = F) = F) = F) = F
# total_2 = not (not a or b and c) # not ((not F = T) or (T and T = T) = T) =F
# print(total, total_1, total_2)

# a, b, c = False, False, True
# total = not (a or not b and c) #not (F or ((not F = T) and T = T) =T) = F
# total_1 = a and not (b and not c) # F and (not(F and (not T = F) = F) = T) = F
# total_2 = not (not a or b and c) # not ((not F = T) or (F and T = F) = T) =F
# print(total, total_1, total_2)

# a, b, c = False, False, False
# total = not (a or not b and c) #not (F or ((not F = T) and F = F) =T) = F
# total_1 = a and not (b and not c) # F and (not(F and (not F = T) = F) = T) = F
# total_2 = not (not a or b and c) # not((not F = T) or (F and F = F) = T) =F
# print(total, total_1, total_2)

# a, b, c = True, False, False
# total = not (a or not b and c) #not (T or ((not F = T) and F = F) =T) = F
# total_1 = a and not (b and not c) # T and (not (F and (not F = T) = F) = T) = T
# total_2 = not (not a or b and c) # not ((not T = F) or (F and F = F) = F) = T
# print(total, total_1, total_2)

# a, b, c = True, True, False
# total = not (a or not b and c) #not (T or ((not T = F) and F = F) =T) = F
# total_1 = a and not (b and not c) # T and (not(T and (not F = T) = T) = F) = F
# total_2 = not (not a or b and c) # not ((not T = F) or (T and F = F) = F) = T
# print(total, total_1, total_2)

# a, b, c = True, False, True
# total = not (a or not b and c) #not (T or ((not F = T) and T = T) =T) = F
# total_1 = a and not (b and not c) # T and (not (F and (not T = F) = F) = T) = T
# total_2 = not (not a or b and c) # not ((not T = F) or (F and T = F) = F) = T
# print(total, total_1, total_2)

# a, b, c = False, True, False
# total = not (a or not b and c) #not (F or ((not T = F) and F = F) =T) = T
# total_1 = a and not (b and not c) # F and (not(T and (not F = T) = T) = F) = F
# total_2 = not (not a or b and c) # not((not F = T) or (T and F = F) = T) = F
# print(total, total_1, total_2)

#Задание 9
# a, b, c = True, True, True
# total = not (a and b) and (not a or not c) # (not(T and T = T) = F) and ((not T = F) or (not T = F) = F) = F
# total_1 = not (a and not b) or (a or not c) # (not(T and (not T = F) = F) = T) or (T or (not T = F) = T) = T
# total_2 = a and not b or not (a or not c) # (T and (not T = F) = F) or (not(T or (not T = F) = T) = F) = F
# print(total, total_1, total_2)

# a, b, c = False, True, True
# total = not (a and b) and (not a or not c) # (not(F and T = F) = T) and ((not F = T) or (not T = F) = T) = T
# total_1 = not (a and not b) or (a or not c) # (not(F and (not T = F) = F) = T) or (F or (not T = F) = F) = T
# total_2 = a and not b or not (a or not c) # (F and (not T = F) = F) or (not (F or (not T = F) = F) = T) = T
# print(total, total_1, total_2)

# a, b, c = False, False, True
# total = not (a and b) and (not a or not c) # (not(F and F = F) = T) and ((not F = T) or (not T = F) = T) = T
# total_1 = not (a and not b) or (a or not c) # (not(F and (not F = T) = F) = T) or (F or (not T = F) = F) = T
# total_2 = a and not b or not (a or not c) # (F and (not F = T) = F) or (not(F or (not T = F) = F) = T) = T
# print(total, total_1, total_2)

# a, b, c = False, False, False
# total = not (a and b) and (not a or not c) # (not (F and F = F) = T) and ((not F = T) or (not F = T) = T) = T
# total_1 = not (a and not b) or (a or not c) # (not (F and (not F = T) = F) = T) or (F or (not F = T) = T) = T
# total_2 = a and not b or not (a or not c) # (F and (not F = T) = F) or (not(F or (not F = T) = T) = F) = F
# print(total, total_1, total_2)

# a, b, c = True, False, False
# total = not (a and b) and (not a or not c) # (not (T and F = F) = T) and ((not T = F) or (not F = T) = T) = T
# total_1 = not (a and not b) or (a or not c) # (not (T and (not F = T) = T) = F) or (T or (not F = T) = T) = T
# total_2 = a and not b or not (a or not c) # (T and (not F = T) = T) or (not (T or (not F = T) = T) = F) = T
# print(total, total_1, total_2)

# a, b, c = True, True, False
# total = not (a and b) and (not a or not c) # (not (T and T = T) = F) and ((not T = F) or (not F = T) = T) = F
# total_1 = not (a and not b) or (a or not c) #(not (T and (not T = F) = F) = T) or (T or (not F = T) = T) = T
# total_2 = a and not b or not (a or not c) # (T and (not T = F) = F) or (not (T or (not F = T) = T) = F) = F
# print(total, total_1, total_2)

# a, b, c = False, True, False
# total = not (a and b) and (not a or not c) # (not (F and T = F) = T) and ((not F = T) or (not F = T) = T) = T
# total_1 = not (a and not b) or (a or not c) #(not (F and (not T = F) = F) = T) or (F or (not F = T) = T) = T
# total_2 = a and not b or not (a or not c) # (F and (not T = F) = F) or (not (F or (not F = T) = T) = F) = F
# print(total, total_1, total_2)

# a, b, c = True, False, True
# total = not (a and b) and (not a or not c) # (not (T and F = F) = T) and ((not T = F) or (not T = F) = F) = F
# total_1 = not (a and not b) or (a or not c) # (not (T and (not F = T) = T) = F) or (T or (not T = F) = T) = T
# total_2 = a and not b or not (a or not c) #(T and (not F = T) = T) or (not (T or (not T = F) = T) = F) = T
# print(total, total_1, total_2)

#Задание 10
#а
# x = 1
# y = -1
# print(x**2 - y**2 <= 0)

#б
# x = 2
# y = -2
# logic = x>=2 or y**2!=4
# print(logic)

#в
# x = 2
# y = 2
# lkg = x>=0 and y**2>4
# print(lkg)

#г
# x = 1
# y = 2
# log = x*y!=4 and y>x
# print(log)

#д
# x = 2
# y = 1
# log = x*y!=0 or x>y
# print(log)

#е
# x = 1
# y = 2
# log = not(x*y<1) and y>x
# print(log)

#ж
x = 2
y = 1
log = not (x*y<0) or y>x
print(log)