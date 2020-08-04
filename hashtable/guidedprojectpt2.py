new_list = [None] * 8


def my_hash(s):
    string_bytes = s.encode()
    total = 0
    for b in string_bytes:
        total += b

    return total


def djb2(self, key):
    hash = 5381
    for element in key:
        hash = (hash * 33) + ord(element)
    return hash
