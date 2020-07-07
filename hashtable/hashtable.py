
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LL:
    def __init__(self):
        #keep track of head
        self.head = None

    def __str__(self):
        r = ""
        cur = self.head

        while cur is not None:
            r += f'({cur.value})'
            if cur.next is not None:
                r += ' -> '

            cur = cur.next

        return r

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def find(self, value):
        current = self.head #keep copy of head
        while current is not None: #traverse LL
            if current.value == value:
                return current
            current = current.next
        return None #not in the LL

    def delete(self, value):
        current = self.head
        #if I'm deleting the head
        if current.value == value:
            self.head = self.head.next
            return current
        
        #it's not the head
        #traverse LL with both pointers
        prev = current
        current = current.next
        
        while current is not None:
            if current.value == value:
                prev.next = current.next
                return current
            else:   
                prev = prev.next
                current = current.next

        return None
        
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.head = None


    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = MIN_CAPACITY
        self.data = [None] * self.capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.data) # or just self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        load_factor = self.load / len(self.data)
        return load_factor
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
        # the modulus keeps it 32-bit, python integers don't overflow
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # get slot
        slot = self.hash_index(key)
        # new entry, instantiate HashTableEntry (like a node)  
        new_entry = HashTableEntry(key, value)
        # if there's something there in that slot:
        if self.data[slot]:
            #append to the head, update pointers
            #My new entry NEXT pointer points to the "head of slot"/"first position"
            new_entry.next = self.data[slot]
            
            #In that first position put there my new entry, making it the "head" of that slot
            self.data[slot] = new_entry 
            self.load += 1
            """ #append to end
            self.data[slot].next = new_entry
            print(" NEXTT!!!", self.data[slot].next) """
        # if slot is empty put there my new entry
        else:
            self.data[slot] = new_entry
            self.load += 1
        #if found, update it
        #if not found, make a new HashTableEntry
        #and add it to the list

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key,None)
        self.load -= 1


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here


    def resize(self, new_capacity):
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
