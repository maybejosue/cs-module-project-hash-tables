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
# singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return current

    def update_or_else_insert_at_head(self, key, value):
        print('in here')
        # check if the key is already in the linked list
        # find the node
        current = self.head
        while current is not None:
            # if key is found, change the value
            if current.key == key:
                current.value = value
                # exit function immediately
                return
            current = current.next

        # if we reach the end of the list, it's not here!
        # make a new node, and insert at head
        new_node = HashTableEntry(key, value)
        new_node.next = self.head
        self.head = new_node


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        # Your code here
<<<<<<< HEAD
=======
        # this creates our list multiplied with the capacity passed in
        self.capacity = [None] * capacity
>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271

    def get_num_slots(self):
        pass
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
<<<<<<< HEAD
=======
        # return length of capacity
        return len(self.capacity)
>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271

    def get_load_factor(self):
        pass
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here

<<<<<<< HEAD
    def fnv1(self, key):
        pass
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

=======
>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271
    def djb2(self, key):
        pass
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        # hash is 5381
        hash = 5381

        # loop through all letters that make up the key
        for letter in key:
            # encode letters to numbers
            hash = (hash * 33) + ord(letter)

<<<<<<< HEAD
=======
        return hash

>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271
    def hash_index(self, key):
        pass
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
<<<<<<< HEAD
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity
=======
        # return self.fnv1(key) % length of self.capacity
        return self.djb2(key) % len(self.capacity)
>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271

    def put(self, key, value):
        pass
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # # Your code here
        # # insert new hash into table
        # new_hash = HashTableEntry(key, value)

        # # hash the key the to receive index in which value will go in
        # hash_index_num = self.hash_index(key)

        # # self.capacity to the index equals node
        # self.capacity[hash_index_num] = new_hash

        # initialize slot as a LL
        ###

<<<<<<< HEAD
=======
        hello = update_or_else_insert_at_head(key, value)
        print(f"this is the hello: {hello}")

>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271
    def delete(self, key):
        pass
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # decode key
        hash_index_num = self.hash_index(key)

<<<<<<< HEAD
=======
        # make sure the value is not equal to none
        if self.capacity[hash_index_num] is not None:
            # if it has a value then reset the value to None
            self.capacity[hash_index_num] = None
        # else return print
        else:
            print("key is already empty")

>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271
    def get(self, key):
        pass
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # decode key
        hash_index_num = self.hash_index(key)

<<<<<<< HEAD
=======
        # make sure the value is not equal to none
        if self.capacity[hash_index_num] is not None:
            # if it has a value return it
            return self.capacity[hash_index_num].value

        # else return
        else:
            return

>>>>>>> b7c1ed7b05956f900811a79ce1b5c575f17f2271
    def resize(self, new_capacity):
        pass
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here


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
