# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        hashindex = self._hash_mod(key)
        if self.storage[hashindex] is None:
            self.storage[hashindex] = LinkedPair(key, value)
        else:
            currentPair = self.storage[hashindex]
            # loop through linked list until you get to the last item of the list
            # if the key matches, however, stop
            while currentPair.next is not None:
                if currentPair.key == key:
                    break
                currentPair = currentPair.next
            
            # if you are at the key, replace its value
            if currentPair.key == key:
                currentPair.value = value
            # otherwise, add a new linked pair at the end
            else:
                currentPair.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        hashindex = self._hash_mod(key)
        if self.storage[hashindex] is None:
            print(f"error: no data with key {key}")
        else:
            currentPair = self.storage[hashindex]
            # if the first key matches the input key, replace the first linked pair with the next linked pair
            if currentPair.key == key:
                self.storage[hashindex] = currentPair.next
            else:
                # find the linked pair before the key you're looking for
                while currentPair.next and currentPair.next.key is not key:
                    currentPair = currentPair.next
                # link the previous linked pair with the next linked pair
                currentPair.next = currentPair.next.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        hashindex = self._hash_mod(key)
        if self.storage[hashindex] is None:
            return None
        else:
            currentPair = self.storage[hashindex]
            while currentPair.key is not key:
                currentPair = currentPair.next
                # make sure you don't loop forever
                if currentPair is None:
                    return None
            return currentPair.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # create a new storage that's double the capacity
        oldStorage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        # loop through the old storage and re-insert every linked pair into the new storage
        for item in oldStorage:
            if item:
                while item is not None:
                    self.insert(item.key, item.value)
                    item = item.next




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
