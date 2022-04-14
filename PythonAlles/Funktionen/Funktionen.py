#Funktionen
def funktion1 (a,b):
    print(a,b)
x = 3
y = 4
funktion1(x,y)

# funktion mit default werten
def funktion2 (a, b = None):  # None = wert wenn sonst keiner übergeben wird
    if b:
        print(a,b)
    else:
        print(a)
funktion2(x, b=35)     # b=35 damit man sieht das es ein Defaultwert ist

#So muss man es machen da es sont zu fehlern kommen kann....
def grow_list(val, my_list=None):   # None da es immer eine neue Liste sein soll
    if my_list:
        my_list.append(val)
    else:
        my_list = [val]
    return my_list

my_list2 = grow_list(42)
print(my_list2)

my_list3 = grow_list(43)
print(my_list3)

# NORMAL ARGS; *ARGS; DEFAULT ARGS
# args = unbekannte anzahl an argumenten werden übergeben
def my_function4(a, *args, b=None):
    print(*args, type(args))
    print('a: {}, b: {}, args: {}'.format(a, b, args))

my_function4(1, 3, 4, b=2)


