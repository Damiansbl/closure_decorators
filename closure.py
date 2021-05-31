def sentence(name):
    age = 36
    lol = 30

    def full_sentence(city):
        return f"I am {name}, {age} years old, from {city}"

    return full_sentence


# s = sentence("Pawel")
# print(s("Krakow"))


# uuid - universal unique identifier
def gen_uuid():
    idx = 0

    def inner():
        nonlocal idx
        result = idx
        idx += 1

        return result

    return inner

x = 10
uuid = gen_uuid()

# _ in range (10):
#    print(uuid())

print(uuid())
print(uuid())
print(uuid())