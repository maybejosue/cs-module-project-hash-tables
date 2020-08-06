class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
# MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # this creates our list multiplied with the capacity passed in
        self.capacity = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        # return length of capacity
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here
        return self.count / self.get_num_slots()

    # def fnv1(self, key):
    #     pass
    #     """
    #     FNV-1 Hash, 64-bit

    #     Implement this, and/or DJB2.
    #     """
    #     # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        # hash is 5381
        hash = 5381

        # loop through all letters in key passed in
        for letter in key:
            # hash is now set to 5381 * 33 and add method ord to letter
            hash = (hash * 33) + ord(letter)

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % length of self.capacity
        return self.djb2(key) % len(self.capacity)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        if self.get_load_factor() >= 0.7:
            self.resize(len(self.capacity) * 2)

        # create a node holding key and value
        new_node = HashTableEntry(key, value)

        # get hash using key
        hash_index = self.hash_index(key)

        # check if self.capacity[hash_index] is None
        if self.capacity[hash_index] is None:
            # then set self.capacity[hash_index] to the new_node
            self.capacity[hash_index] = new_node
            self.count += 1

        # set current to self.capacity[hash_index]
        current = self.capacity[hash_index]

        # while loop (True)
        while True:
            # check if current.next is None
            if current.key == key:
                current.value = value
                break

            if current.next is None:
                # then set current.next to new_node
                current.next = new_node
                self.count += 1
                # break
                break

            # set current to current.next
            current = current.next

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
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
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
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
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
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
