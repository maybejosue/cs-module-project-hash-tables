def word_count(s):
    # Your code here
    # create new cache to empty dictionary
    cache = {}
    # set word_list variable to s.lower().split()
    word_list = s.lower().split()
    # to sanitize all words
    # for loop each word in word_list
    for word in word_list:
        # set i to 0
        i = 0

        # while loop while i < length of word - 1
        while i < len(word) - 1:
            # check if word[i] in [", :, ;, ,, ., -, +, =, /, \, |, [, ], {, }, (, ), *, ^, &] to remove symbols
            # if word[i] in [", :, ;, ,, ., -, +, =, /, \, |, [, ], {, }, (, ), *, ^, &]:
            # problem with remove symbols
            #  word.insert(i, "") inset an empty space at current index

            # add 1 to i

            # to add into cache or add one
            # for loop each word in word_list
            # check if word in cache
            # then add 1 to cache[word]

            # create new key in cache with cache[word] = 1


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
