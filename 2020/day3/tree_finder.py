#!/usr/bin/python

def get_trees_in_path(x_incr, y_incr, tree_list):
    tree_count = 0
    x = 0
    y = 0
    while y < len(tree_list):
        tree_count += 1 if tree_list[y][x] == '#' else 0
        x += x_incr
        y += y_incr
        # mod so that we loop around when we reach the end of a row
        x = x % 31
    return tree_count


def main():
    f = open("input", "r")
    tree_list = f.read()
    if tree_list:
        tree_list = tree_list.splitlines()
        a = get_trees_in_path(1, 1, tree_list)
        b = get_trees_in_path(3, 1, tree_list)
        c = get_trees_in_path(5, 1, tree_list)
        d = get_trees_in_path(7, 1, tree_list)
        e = get_trees_in_path(1, 2, tree_list)
    print("{}".format(a * b * c * d * e))


if __name__ == "__main__":
    main()
