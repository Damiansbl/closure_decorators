def add(a, b):
    b += 3
    return a + b


def calculate_result(a, b):
    x = add(a, b)

    return x * 3


z = calculate_result(4, 5)
print(z)


def my_power(digit):
    return digit ** 2


print(my_power(5))


def my_power(exponent):
    def inner(digit):
        return digit ** exponent

    return inner


power_3 = my_power(3)
power_4 = my_power(4)
power_7 = my_power(7)

print(power_3(2))
print('power 3, what is in closure',
      power_3.__closure__[0].cell_contents)
print(power_4(2))
print('power 4, what is in closure',
      power_4.__closure__[0].cell_contents)
print(power_7(2))
print('power 7, what is in closure',
      power_7.__closure__[0].cell_contents)
