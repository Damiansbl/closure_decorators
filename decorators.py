# Decorator
def upper_decorator(fn):
    def inner(name):
        return fn(name.title())

    return inner


def upper(fn, value):
    return fn(value.title())

@upper_decorator
def hello(name):
    return f"hello {name.title()}"

@upper_decorator
def goodbye(name):
    return f"Goodbye {name.title()}"

# print(upper(hello, "pawel"))
# print(upper(goodbye, "pawel"))


# u = upper_decorator(hello)
# print(u("pawel"))

# g = upper_decorator(goodbye)
# print(g("damian"))

# print(upper_decorator(hello)("damian"))

print(hello("damian"))