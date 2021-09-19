#!/usr/bin/env python3


def upper(input_arr):
    if len(input_arr) == 2:
        return input_arr[1]
    slicepoint = int((len(input_arr)/2))
    return input_arr[slicepoint:]


def lower(input_arr):
    if len(input_arr) == 2:
        return input_arr[0]
    slicepoint = int((len(input_arr)/2))
    return input_arr[:slicepoint]


def process_input(boarding_input, input_type):
    input_options = {
        'row': list(range(0, 128)),
        'col': list(range(0, 8)),
    }
    options = {
        'F': lower,
        'L': lower,
        'B': upper,
        'R': upper,
    }
    output = input_options.get(input_type)
    for bi in boarding_input:
        output = options.get(bi)(output)
    return output


def find_my_seat(assigned_seats, id_list):
    for row, col_nums in assigned_seats.items():
        row_map = dict.fromkeys(list(range(0, 8)), 1)
        if len(col_nums) < 8:
            for seat in col_nums:
                row_map.pop(seat)
            if row_map:
                for col_num in row_map.keys():
                    id = (row * 8) + col_num
                    if (id + 1) in id_list and (id - 1) in id_list:
                        return id


def main():
    f = open("input", "r", encoding="utf-8")
    boarding_assignments = f.read()
    if boarding_assignments:
        assigned_seats = {}
        id_list = []
        boarding_assignments = boarding_assignments.splitlines()
        highest_id = 0
        for ba in boarding_assignments:
            row = process_input(ba[:7], 'row')
            col = process_input(ba[7:], 'col')
            bp_id = (row * 8) + col
            if bp_id > highest_id:
                highest_id = bp_id
            if assigned_seats.get(row):
                assigned_seats[row].append(col)
                id_list.append(bp_id)
            else:
                assigned_seats[row] = [col]
                id_list.append(bp_id)
        my_seat = find_my_seat(assigned_seats, id_list)
        p = "Highest Seat ID: {}".format(
                highest_id)
        print(p)
        print("My Seat: {}".format(my_seat))
    f.close()


if __name__ == "__main__":
    main()
