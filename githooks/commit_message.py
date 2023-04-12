#!/usr/bin/env python

import re
import sys
from rules import commit_message_rules


def main():
    print('Executing the commit message rule.')
    with open(sys.argv[1], "r") as fp:
        lines = fp.readlines()

        for idx, line in enumerate(lines):
            if line[0] == "#":
                continue

            if not line_valid(idx, line):
                show_rules()
                sys.exit(1)

    sys.exit(0)


def line_valid(idx, line):
    if idx == 0:
        regex_pattern = '^Issue-\\d{1,3}: .+$'
        return re.match(regex_pattern, line)
    elif idx == 1:
        return len(line.strip()) == 0
    else:
        return len(line.strip()) <= 120


def show_rules():
    print(commit_message_rules)


if __name__ == "__main__":
    main()
