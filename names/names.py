import time

# Inserting n elements in BST is... nlog(n)
# Using BST for log_2(n) search times.
# Searching n elements will be nlog(n)
# Runtime = 2nlog(n) = nlog(n)
class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        else:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else: return False
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else: return False

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


name_tree = BinarySearchTree(names_1[0])

for i in range(1, len(names_1)):
    name_tree.insert(names_1[i])
    
for n in names_2:
    if name_tree.contains(n):
        duplicates.append(n)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
