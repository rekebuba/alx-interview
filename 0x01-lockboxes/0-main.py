#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

# Test case 1: All boxes can be unlocked
boxes = [[1, 2, 3], [0], [4], [2, 4], [3, 5]]
print(canUnlockAll(boxes))  # Expected Output: True

# Test case 2: One box is isolated and cannot be unlocked
boxes = [[1, 3], [2], [4], [5], [], [6]]
print(canUnlockAll(boxes))  # Expected Output: True

# Test case: One box is isolated and cannot be unlocked
boxes = [[1, 2], [], [3], [4], []]
print(canUnlockAll(boxes))  # Expected Output: False

# Test case 3: Starting box contains all keys
boxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
print(canUnlockAll(boxes))  # Expected Output: True

# Test case 4: No keys in the starting box
boxes = [[], [1, 2, 3], [4], [5], [6], []]
print(canUnlockAll(boxes))  # Expected Output: False

# Test case 5: Large number of boxes, all unlockable
boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50]]
print(canUnlockAll(boxes))  # Expected Output: True

# Test case 6: Large number of boxes, one box isolated
boxes = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], []]
print(canUnlockAll(boxes))  # Expected Output: False

# Test case 7: Complex dependencies
boxes = [[1], [2, 3], [3, 4], [5], [0, 2, 3], [6, 7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], [41], [42], [43], [44], [45], [46], [47], [48], [49], [50]]
print(canUnlockAll(boxes))  # Expected Output: True

# Test case 8: Disjoint subgroups of boxes
boxes = [[1, 2], [0], [], [], [5, 6], [4], [4]]
print(canUnlockAll(boxes))  # Expected Output: False
