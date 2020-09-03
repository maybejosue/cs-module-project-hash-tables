def no_dups(s):
    if len(s) < 1:
        return s

    cache = {}
    result = []
    clean = s.split()

    for word in clean:
        if word not in cache:
            cache[word] = 0

    for word in cache:
        result.append(word)

    return ' '.join(result)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
