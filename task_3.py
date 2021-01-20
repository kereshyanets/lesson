
def my_f(a,b,c):
    return max(a + b, c + a, b + c)
a = int(input('введите первое число: '))
b = int(input('введите второе число: '))
c = int(input('введите третье число: '))


numbers = my_f(a,b,c)
print(numbers)