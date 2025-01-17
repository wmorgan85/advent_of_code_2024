from common.parser import parse_input
from common.script_path import get_caller_file_path as get_local_path


def solve(list_one: list[int], list_two: list[int]) -> int:

    if (list_one is None) or (list_two is None):
        raise AssertionError("Lists must not be None.")

    if len(list_one) != len(list_two):
        raise AssertionError("Lists must have the same length.")

    return sum(abs(a - b) for a, b in zip(sorted(list_one), sorted(list_two)))


def run():
    input_file = get_local_path("input.txt")
    list_one, list_two = parse_input(input_file)
    return solve(list_one, list_two)


if __name__ == "__main__":
    print("Day 1, Part 1:", run())
