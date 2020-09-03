def word_count(s):

    if len(s) < 1:
        return {}

    cache = {}
    s_to_arr = s.lower().split()
    print(s_to_arr)

    for word in s_to_arr:
        if word.isalnum() and word in cache:
            cache[word] += 1

        if word.isalnum() and word not in cache:
            cache[word] = 1

        if word.isalnum() is False:
            new_string = ''
            print(word)
            for letter in word:
                if letter not in ' " : ; , . - + = / \ | [ ] { } ( ) * ^ &':
                    new_string += letter
            if len(new_string) < 1:
                return {}
            if new_string not in cache:
                cache[new_string] = 1
            else:
                cache[new_string] += 1
    print(cache)
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello. hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
