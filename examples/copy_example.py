import copy

test_1 = [1, 2, 3, [1, 2, 3]]
# test_copy = copy.copy(test_1)
test_copy = copy.deepcopy(test_1)

print(test_1, test_copy)
test_copy[3].append(4)

print(test_1, test_copy)