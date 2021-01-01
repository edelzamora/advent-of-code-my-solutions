
map = open('map.txt', 'r').readlines()


def traverse_map(map):
    landscape = []
    for line in map:
        landscape.append(line.strip())
    trees_passed = 0
    index = 0
    for array in range(len(landscape)):
        for elem in range(index, len(landscape[array]), 3):
            index += 3
            if index >= len(landscape[array]):
                diff = index - len(landscape[array])
                index = diff
            if landscape[array][elem] == '#':
                trees_passed += 1
            break
    return trees_passed

print(traverse_map(map))

#Part 2 below - - - -

def traverse_map_different_distance(map, right, down):
    landscape = []
    for line in map:
        landscape.append(line.strip())
    tree_passed = 0
    index = 0
    for array in range(0, len(landscape), down):
        for elem in range(index, len(landscape[array]), right):
            index += right
            if index >= len(landscape[array]):
                diff = index - len(landscape[array])
                index = diff
            if landscape[array][elem] == '#':
                tree_passed += 1
            break
    return tree_passed

def calculation_of_slopes(slope1, slope2, slope3, slope4, slope5):
    return slope1 * slope2 * slope3 * slope4 * slope5

print(calculation_of_slopes(
    traverse_map_different_distance(map, 1, 1),
    traverse_map(map),
    traverse_map_different_distance(map, 5, 1),
    traverse_map_different_distance(map, 7, 1),
    traverse_map_different_distance(map, 1, 2)))