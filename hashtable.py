#!python

import math
from linkedlist import LinkedList
# from __future__ import division #if using older python (ex. python 2)


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    #hihi
    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        #when using python2, must cast either self.size or len(self.buckets) as a float
        #load factor = # entries / # buckets. thus,
        return self.size / len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            #the bucket.items() parameter is from the LINKEDLIST items() method
            #can be kinda confusing because, lol, we're inside another items() method 👥
            #but there is an IMPORTANT❗️distinction
            all_items.extend(bucket.items()) #extend=append many times, for many items
                                            #while with 'append' just 1 at a time
            # all_items += bucket.items() #outputs the same as above. BUTBUTBUT!!!
                                            #for +=, you must
                                                #1 make new array
                                                #2 reassign var,
                                            #and so needs more time+memory. 👎🏼
                                            #extend exists to tackle 🥊 this problem 
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Count number of key-value entries in each of the buckets
        item_count = 0
        for bucket in self.buckets:
            item_count += bucket.length()
        return item_count
        # Equivalent to this list comprehension:
        return sum(bucket.length() for bucket in self.buckets)

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
 
        #🐴hollyhock voice: idk, IS there an entry in this bucket with this key?
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # if entry is not None: #not none = it exists, and we're updating it #HAHAHA I FOUND A BETTER WAY 🎉😁🎉
        if self.contains(key) is True:
            bucket.delete(entry) #remove key-val entry from bucket BEFORE appending
            #DON'T UPDATE SELF.SIZE HERE - already addressed IN delete()!
        else: #without deleting, we must increment size by +1
            self.size += 1 #we're NOT doing so if we end up deleting, hence 'else'
        bucket.append((key, value)) #insert new key-val entry into bucket no matter what

        if self.load_factor() > 0.75: #load factor approaching 1? RESIZE to reduce it
            self._resize()


    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]

        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            bucket.delete(entry)
            self.size -= 1 #deletion = entry gone. byebye. size reduction
        else:
            raise KeyError('Key not found: {}'.format(key))

    #hihi
    #the _ is the equivalent of 'private' - says this is an internal method only to be called within the class, so don't call it outside.
    #not to be confused with __, i.e. mangle, which makes it even more private lol
    #alan says 'seriously guys don't touch this' (this='mangle')
    def _resize(self, bucket_quantity=None):
        #❗️i renamed the non-self param because 'new_size' was tripping me up HARD
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key).
        Best and worst case running time: ??? under what conditions? [TODO]
        Best and worst case space usage: ??? what uses this memory? [TODO]"""
        # If unspecified, choose new size dynamically based on current size
        if bucket_quantity is None:
            bucket_quantity = len(self.buckets) * 2  #2x size will 0.5x-ify load factor

        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif bucket_quantity is 0:
            bucket_quantity = math.floor(len(self.buckets) / 2)  # Half size

        entries = self.items() #list to temporarily hold all current key-val entries
        self.buckets = [LinkedList() for _ in range(bucket_quantity)] #reset buckets w/ bucket_quantity as guidance
        self.size = 0 #reset # of entries before appending key-val pairs

        #look how short and nice it is!!! <3
        for key, value in entries: #each entry is a lil linked list
            self.set(key, value) #inserts key-val entry into new list of buckets, which'll rehash based on the new size
        # # Python lets us do the above ^ which is the shortened ver of:
        # for entry in entries:
        #     key, value = entry
        #     self.set(key, value)

        # #the OG way
        # for entry in entries:
        #     key = entry[0]
        #     value = entry[1]
        #     self.set(key, value)

def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
