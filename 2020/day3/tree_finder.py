#!/usr/bin/python

def main():
    """
    Rules:
    # is a tree
    . is an open space

    Task: count the trees you encounter by starting at 0,0
    and moving 3 right 1 down.  Loop to beginning of row at the edges
    """
    f = open("input", "r")
    tree_list = f.read()
    tree_count = 0

    # coordinates
    x = 0
    y = 0

    if tree_list:
        tree_list = tree_list.splitlines()
        while y < len(tree_list):
            tree_count += 1 if tree_list[y][x] == '#' else 0
            y += 1
            x += 3
            x = x % 31
    print(tree_count)


if __name__ == "__main__":
    main()
