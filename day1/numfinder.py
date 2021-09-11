#!/usr/bin/python

def main():
    print("Part One: " + str(find_answer_from_file_pt_one("input")))
    print("Part Two: " + str(find_answer_from_file_pt_two("input")))


if __name__ == "__main__":
    main()


def find_answer_from_file_pt_one(file_name):
    f = open(file_name, "r")
    num_list = [int(num) for num in f.read().splitlines()]
    for n in num_list:
        temp = 2020 - n
        if temp > 0:
            if temp in num_list:
                return(temp * n)


def find_answer_from_file_pt_two(file_name):
    f = open(file_name, "r")
    num_list = ([int(num) for num in f.read().splitlines()])
    for i, n in enumerate(num_list):
        new_base = 2020 - n
        for entry in num_list[i:]:
            fin = new_base - entry
            if fin > 0 and fin in num_list:
                return n * fin * entry



