queue = []


def add_to_queue(item):
    queue.append(item)


def remove_from_queue():
    queue.pop(0)


stack = []


def add_to_stack(item):
    stack.append(item)


def remove_from_stack():
    stack.pop()


print(stack)
add_to_stack("a")
add_to_stack("b")
add_to_stack("c")
print(stack)
remove_from_stack()
print(stack)
remove_from_stack()
print(stack)
