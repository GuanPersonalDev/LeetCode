import random


class RandomizedSet:
    def __init__(self):
        self.map = {}
        self.data = []
    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        i = self.map.pop(val)
        l = len(self.data) - 1
        if i != l:
            self.map[self.data[l]] = i
            self.data[i] = self.data[l]
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomized_set = RandomizedSet()
print(randomized_set.insert(0))
print(randomized_set.remove(0))
print(randomized_set.insert(0))
# print(randomized_set.remove(0))
# print(randomized_set.insert(2))
# print(randomized_set.remove(1))
# print(randomized_set.getRandom())
