a = int(input('введите первое число: '))
b = int(input('введите второе число: '))



def my_f(a):
    a /= b
    return a
a = my_f(a)
print(a)