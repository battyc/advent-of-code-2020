#!/usr/bin/env python3

import json
import re


class Passport():
    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    @property
    def byr(self):
        return self._byr

    @byr.setter
    def byr(self, val):
        if not val or val < 1920 or val > 2002:
            raise ValueError("Bad byr")
        self._byr = val

    @property
    def iyr(self):
        return self._iyr

    @iyr.setter
    def iyr(self, val):
        if not val or val < 2010 or val > 2020:
            raise ValueError("Bad iyr")
        self._iyr = val

    @property
    def eyr(self):
        return self._eyr

    @eyr.setter
    def eyr(self, val):
        if not val or val < 2020 or val > 2030:
            raise ValueError("Bad eyr")
        self._eyr = val

    @property
    def hgt(self):
        return self._hgt

    @hgt.setter
    def hgt(self, val):
        exp = r'^([0-9]+)(cm|in)$'
        match = re.match(exp, val) if val else None
        if not match:
            raise ValueError("Bad hgt")
        else:
            value = int(match.groups()[0])
            unit = match.groups()[1]
            if unit == "cm":
                if value < 150 or value > 193:
                    raise ValueError("Bad hgt")
            elif unit == "in":
                if value < 59 or value > 76:
                    raise ValueError("Bad hgt")

        self._hgt = val

    @property
    def hcl(self):
        return self._hcl

    @hcl.setter
    def hcl(self, val):
        exp = r'^#[0-9a-f]{6}$'
        if not val or not re.match(exp, val):
            raise ValueError("Bad hcl")
        self._hcl = val

    @property
    def ecl(self):
        return self._ecl

    @ecl.setter
    def ecl(self, val):
        opt = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not val or val not in opt:
            raise ValueError("Bad ecl")
        self._ecl = val

    @property
    def pid(self):
        return self._pid

    @pid.setter
    def pid(self, val):
        exp = r'^[0-9]{9}$'
        if not val or not re.match(exp, val):
            raise ValueError("Bad pid")
        self._pid = val


def is_valid_passport(passport):
    try:
        Passport(
            int(passport.get('byr')) if passport.get('byr') else None,
            int(passport.get('iyr')) if passport.get('iyr') else None,
            int(passport.get('eyr')) if passport.get('eyr') else None,
            passport.get('hgt'),
            passport.get('hcl'),
            passport.get('ecl'),
            passport.get('pid'),
            passport.get('cid')
        )
        return True
    except ValueError:
        return False


def main():
    f = open("input", "r", encoding="utf-8")
    passports = f.read()
    valid_passports = 0
    if passports:
        passports = passports.split('\n\n')
        for p in passports:
            p = json.loads("{}{}{}".format(
                '{"',
                p.replace('\n', ' ').replace(' ', '", "').replace(':', '":"'),
                '"}'))
            valid_passports += 1 if is_valid_passport(p) else 0
        print(valid_passports)
    f.close()


if __name__ == "__main__":
    main()
