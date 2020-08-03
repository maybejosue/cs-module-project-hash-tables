my_list = ["hi", "how", "are", "you", "hello", "world"]


def my_hash(l):
    string_bytes = l.encode()
    total = 0
    for letter in string_bytes:
        total += letter

    return total


new_list = [None] * 8

# How to put / insert a value to a key
hello_hash = my_hash("hello")
hello_index = hello_hash % len(new_list)
# print(hello_index)
new_list[hello_index] = 'hello world'
# print(new_list)
# print(hello_index)
# print(hello_hash)


hashed_world = my_hash('world')
world_index = hashed_world % len(new_list)
# print(world_index)
new_list[world_index] = 'howdy world'
# print(new_list)
# print(hello_index)
# print(hello_hash)

# How to search for a value
hashed_string = my_hash('hello')
our_index = hashed_string % len(new_list)
# print(new_list[our_index])


def djb2(key):
    hash = 5381
    for c in key:
        hash = (hash * 33) + ord(c)
    return hash


print(djb2('hello world'))
