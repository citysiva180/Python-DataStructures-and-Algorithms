class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    # Its a hash method which adds the address to the value we would pass.

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash+ord(letter)*23) % len(self.data_map)
            return my_hash

    def print_tables(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])


# to get the ascii value numberically we could use the ord letter method
# using the modulo,

# You should always have a prime number
# Prime number increases no of randomness reducing collisions

# In hash, we upfront talk about the size and the allocation of values
# to that size we add values with addresses... Also values would be dictionary or list

my_hash_table = HashTable()


my_hash_table.set_item("bolts", 4000)
my_hash_table.set_item("Nuts", 4000)
my_hash_table.set_item("wires", 4000)
my_hash_table.set_item("fibre Optics", 4000)

my_hash_table.print_tables()
