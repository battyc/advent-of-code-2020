#!/usr/bin/python

import re


def evaluate_password(password_line):
    rule_expression = r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
    low, high, letter, password = re.match(
        rule_expression, password_line).groups()
    total_letter = password.count(letter)
    if total_letter >= int(low) and total_letter <= int(high):
        return 1
    return 0


def main():
    f = open("input", "r")
    password_list = f.read().splitlines()
    total = 0
    for p in password_list:
        total += evaluate_password(p)
    print(total)


if __name__ == "__main__":
    main()
