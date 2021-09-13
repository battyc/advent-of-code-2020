#!/usr/bin/env python3

import re


def evaluate_sled_policy_password(password_line):
    rule_expression = r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
    low, high, letter, password = re.match(
        rule_expression, password_line).groups()
    total_letter = password.count(letter)
    if total_letter >= int(low) and total_letter <= int(high):
        return 1
    return 0


def evaluate_toboggan_policy_password(password_line):
    rule_expression = r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'
    low, high, letter, password = re.match(
        rule_expression, password_line).groups()
    p1 = password[int(low)-1]
    p2 = password[int(high)-1]
    if (p1 == letter and p2 != letter) or (p2 == letter and p1 != letter):
        return 1
    return 0


def main():
    f = open("input", "r")
    password_list = f.read().splitlines()
    sled_total = 0
    toboggan_total = 0
    for p in password_list:
        sled_total += evaluate_sled_policy_password(p)
        toboggan_total += evaluate_toboggan_policy_password(p)
    print("Sled Total: {}".format(sled_total))
    print("Toboggan Total: {}".format(toboggan_total))


if __name__ == "__main__":
    main()
