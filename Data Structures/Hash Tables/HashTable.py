class HashTable():
    def __init__(self, len):
        self.data = [None for _ in range(len)]
        pass

    def set(self, key, value):
        t = self._hash(key)
        if self.data[t] is None:
            self.data[t] = [[key, value]]
        else:
            self.data[t].append([key, value])

    def get(self, key):
        temp = self._hash(key)
        for i in self.data[temp]:
            if i[0] == key:
                return i[1]

    def _hash(self, key):
        hash1 = 0
        for i in range(0, len(key)):
            hash1 = (hash1 + ord(key[i]) * i) % len(self.data)
        return hash1


    # Get all the keys
    def get_keys(self):
        keys = []
        for i in self.data:
            if i is not None:
                if len(i) > 1:
                    for j in i:
                        keys.append(j[0])
                else:
                    keys.append(i[0][0])

        return keys


hash1 = HashTable(100)
hash1.set("Nik", "nn")
hash1.set("abc", "aa")
hash1.set("bcd", "bb")
hash1.set("cde", "cc")

# Both have same hash value
hash1.set("1", "one")
hash1.set("2", "two")

print(hash1.data)

print(hash1.get("Nik"))
print(hash1.get("abc"))
print(hash1.get("bcd"))
print(hash1.get("cde"))
print(hash1.get("1"))
print(hash1.get("2"))



print(hash1.get_keys())
