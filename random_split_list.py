# There's a webapp version at index.thml

import random

def split_list_into_groups(incl, m):
    # Shuffle the list randomly
    random.shuffle(incl)
    
    # Calculate the size of each group
    n = len(incl)
    print("Total elements to include:",n)

    group_sizes = [n // m + (1 if i < n % m else 0) for i in range(m)]
    print("Number of groups:", m)
    print("Max elements for a single group:", max(group_sizes),'\n')
    
    # Distribute elements into groups and sort each group in ascending order
    groups = []
    start = 0
    for size in group_sizes:
        groups.append(incl[start:start + size])
        start += size

    for group in groups:
        group.sort()
    
    return groups

# Example usage
# incl = [123,123,123,123]
# m = 2

# Read input from file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Convert the input data to a list of integers
incl = list(map(int, lines[0].strip().split(',')))

# Read the number of groups
m = int(lines[1].strip())

groups = split_list_into_groups(incl, m)

# Print the element of all groups separated by new line, add an extra line at the end of each group
for n in range(len(groups)):
    print("Group", n+1)
    print('\n'.join(map(str, groups[n])))
    print()