import os

directory = "./TestStorage"

tree = os.walk(directory)

for dir in tree:
    print(dir)

# print("List of files", tree[1])
# print("List of directories", tree[2])
