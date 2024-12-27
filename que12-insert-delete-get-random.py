class RandomizedSet:

    def __init__(self):
        self.data = []  # List to store the elements
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        
        # Add the value to the list and store its index in the map
        self.index_map[val] = len(self.data)
        self.data.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        
        # Get the index of the element to remove
        index_to_remove = self.index_map[val]
        last_element = self.data[-1]  # The last element in the list

        # Swap the last element with the element to remove
        self.data[index_to_remove] = last_element
        self.index_map[last_element] = index_to_remove

        # Remove the last element
        self.data.pop()
        del self.index_map[val]
        return True

        

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()