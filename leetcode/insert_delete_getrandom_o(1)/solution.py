class RandomizedSet:
    import random 
    def __init__(self):
        self.map_key_to_idx = {}
        self._array = []

    def insert(self, val: int) -> bool:
        if val in self.map_key_to_idx:
            return False

        self.map_key_to_idx[val] = len(self._array)
        self._array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map_key_to_idx:
            return False

        remove_idx = self.map_key_to_idx.get(val)
        self.map_key_to_idx.pop(val)

        if len(self._array) == 1 or remove_idx == len(self._array) - 1:
            self._array.pop()
            return True

        swap = self._array.pop()
        self.map_key_to_idx[swap] = remove_idx     
        self._array[remove_idx] = swap
        return True


    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self._array) - 1)
        return self._array[random_idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()