# Creates a node essentially, but with key and value property and a pointer.
class HashTableEntry:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Handles loop up via O(1) operation
class HashTable:
    # initializes HashTable call via empty arr and counter

    def __init__(self, capacity):
        self.capacity = [None] * capacity
        self.count = 0

# return the length of the initialized arr
    def get_num_slots(self):
        return len(self.capacity)


# load factor is the count / the length of the array

    def get_load_factor(self):
        return self.count / self.get_num_slots()

    # def fnv1(self, key):
    #     pass
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """
    #     # Your code here


# djb2 hash function returns a string into a hashed number

    def djb2(self, key):
        hash = 5381

        for letter in key:
            hash = (hash * 33) + ord(letter)

        return hash

# hash_index is a function that divides a hash string by the length of the initialize arr to return an index #
    def hash_index(self, key):
        return self.djb2(key) % len(self.capacity)

# put function essentialy preforms the entire flow
    def put(self, key, value):
        # checks load factor and resizes based on how many items the array is occupying
        if self.get_load_factor() >= 0.7:
            self.resize(len(self.capacity) * 2)

        # create a node holding key and value
        new_node = HashTableEntry(key, value)

        # get hash using key
        hash_index = self.hash_index(key)

        # check if self.capacity[hash_index] is None
        if self.capacity[hash_index] is None:
            # if spot is empty, then set self.capacity[hash_index] to the new_node
            self.capacity[hash_index] = new_node
            self.count += 1

        # set current as the node thats already in that index
        current = self.capacity[hash_index]

        # while loop (True)
        while True:
            # if there is already a value then override it
            if current.key == key:
                current.value = value
                break

            # if current . next is none and key does not exist, insert it at the tail
            if current.next is None:
                # then set current.next to new_node
                current.next = new_node
                self.count += 1
                # break
                break

            # set current to current.next
            current = current.next

# checks for multipe conditions, if slot in arr, is empty, also if it is tied as a linked list
    def delete(self, key):
        # set hash_index_num to self.hash_index(key)
        hash_index = self.hash_index(key)

        if self.capacity[hash_index] is None:
            return print("Key is not found")

        current = self.capacity[hash_index]

        while True:
            if current.key == key:
                current.value = None
                break

            if current.next is None and current.key != key:
                return print('hey, key is not found')

            current = current.next

    def get(self, key):
        # set hash_index_num to hash_index(key)
        hash_index = self.hash_index(key)

        if self.capacity[hash_index] is None:
            return

        current = self.capacity[hash_index]

        # while loop (True)
        while True:
            # check if current.next is None
            if current.next is None and current.key != key:
                return

            if current.key == key:
                # then set current.next to new_node
                return current.value

            # set current to current.next
            current = current.next

    def resize(self, new_capacity):
        # set old_list_copy to self.capacity
        old_list_copy = self.capacity
        # set self.capacity to [None] * (len(old_list_copy) * new_capacity)
        self.capacity = [None] * new_capacity

        # for loop (old_list_copy)
        for item in old_list_copy:
            # check if item in array is not none
            if item is not None:
                # new_list_hash_idx = self.hash_index(item.key)
                new_list_hash_idx = self.hash_index(item.key)
                #self.capacity[new_list_hash_idx] = item
                self.capacity[new_list_hash_idx] = item


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
