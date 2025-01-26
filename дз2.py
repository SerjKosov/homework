#Задание 2.8
print("Задание 2.8")
a = int(input("Введите трехзначное число: "))
digit = a%10
tens = a//10%10
hundred = a//100
print("Кол-во единиц = ", digit)
print("Кол-во десятков = ", tens)
print(f"сумма цифр в числе {a} равна {tens+digit+hundred}, \nпроизведение равно {digit*tens*hundred}")

#Задание 2.9
print("Задание 2.9")
a = int(input("Введите трехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100
print(digit, tens, hundred, sep='')

#Задание 2.10
print("Задание 2.10")
a = int(input("Введите трехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100
print(tens, digit, hundred, sep='')

#Задание 2.11
print("Задание 2.11")
a = int(input("Введите трехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100
print(digit, hundred, tens, sep='')

#Задание 2.12
print("Задание 2.12")
a = int(input("Введите трехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100
print(tens, hundred, digit, sep='')

#Задание 2.13
print("Задание 2.13")
a = int(input("Введите трехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100
print(hundred, digit, tens,  sep='')

#Задание 2.14
print("Задание 2.14")
a = int(input("Введите трехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100
print(digit, tens, ", ", digit, hundred, ", ", tens, hundred, ", ",
      tens, digit, ", ", hundred, digit, ", ", hundred, tens, sep='')

#Задание 2.15
print("Задание 2.15")
a = int(input("Введите четырехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100%10
thousand = a//1000
print(f'Сумма чисел в цифре {a} равна {digit+tens+hundred+thousand},'
      f' произведение чисел = {digit*tens*hundred*thousand}')

#Задание 2.16
print("Задание 2.16")
a = int(input("Введите четырехзначное число : "))
digit = a%10
tens = a//10%10
hundred = a//100%10
thousand = a//1000
print(hundred*1000 + thousand*100 + digit * 10 + tens)
print(thousand*1000+tens*100+hundred*10+digit)
print(tens*1000+digit*100+thousand*10+hundred)

#Задание 2.17
print("Задание 2.17")
a = int(input("Введите двухзначное число : "))
print(f'В числе {a} единиц: {a%10}, десятков: {a//10%10}')

#Задание 2.18
print("Задание 2.18")
a = int(input("Введите трехзначное число : "))
print(f'В числе {a} десятков {a//10%10}, сотен {a//100%10}')

#Задание 2.19
print("Задание 2.19")
a = int(input("Введите четырехзначное число : "))
hundred = a//100%10
thousand = a//1000%10
print("Сотен:", hundred, "тысяч:", thousand)
print(f'В числе {a} сотен {a//100%10}, тысяч {a//1000%10}')
