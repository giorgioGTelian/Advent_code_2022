
import pathlib
import re
import sys

from math import prod
from typing import TypeAlias

# Typing aliases
Monkeys: TypeAlias = list[dict[str, list]]


def parse(puzzle_input: str) -> Monkeys:
    """Parse input"""
    monkeys: Monkeys = []
    lines: list[str] = puzzle_input.splitlines()
    for line in lines:
        match = re.search(r"Monkey (\d+):", line)
        if match:
            monkey = {"number": match.group(1)}
            monkeys.append(monkey)
        match = re.search(r"Starting items: (.*)", line)
        if match:
            items = [int(item) for item in match.group(1).split(",")]
            monkey["starting_items"] = items
        match = re.search(r"Operation: new = old (.*)", line)
        if match:
            operands = tuple([op for op in match.group(1).split(" ")])
            monkey["operation"] = operands
        match = re.search(r"Test: divisible by (\d+)", line)
        if match:
            monkey["test"] = [int(match.group(1))]
        match = re.search(r"If true: throw to monkey (\d+)", line)
        if match:
            monkey["test"].append(match.group(1))
        match = re.search(r"If false: throw to monkey (\d+)", line)
        if match:
            monkey["test"].append(match.group(1))
            monkey["test"] = tuple(monkey["test"])
    for monkey in monkeys:
        monkey["count"] = 0
    return monkeys


def inspect(item: int, operation: str, value: str, divisor: bool = True) -> int:
    """Do operation on item; return its solution"""
    if value == "old":
        value = item
    match operation:
        case "+":
            item = item + int(value)
        case "*":
            item = item * int(value)
    if divisor:
        return item // 3
    else:
        return item


def test_monkey(item: int, test: int, dest1: str, dest2: str) -> int:
    """Check if item meets monkey test; return number of monkey to throw to"""
    if item % test == 0:
        return int(dest1)
    else:
        return int(dest2)


def part1(monkeys: Monkeys) -> int:
    """Solve part 1"""
    for _ in range(20):
        for monkey in monkeys:
            monkey["starting_items"] = [
                inspect(item, *monkey["operation"]) for item in monkey["starting_items"]
            ]
            for item in monkey["starting_items"]:
                dest: int = test_monkey(item, *monkey["test"])
                monkeys[dest]["starting_items"].append(item)
            monkey["count"] += len(monkey["starting_items"])
            monkey["starting_items"] = []
    counts: list[int] = [monkey["count"] for monkey in monkeys]
    first: int
    second: int
    first, second = sorted(counts)[-2:]
    return first * second


def part2(monkeys: Monkeys) -> int:
    """Solve part 2"""
    tests: list[int] = [monkey["test"][0] for monkey in monkeys]
    supermodulo: int = prod(tests)
    for _ in range(10000):
        for monkey in monkeys:
            monkey["starting_items"] = [
                inspect(item, *monkey["operation"], False)
                for item in monkey["starting_items"]
            ]
            for item in monkey["starting_items"]:
                item %= supermodulo
                dest = test_monkey(item, *monkey["test"])
                monkeys[dest]["starting_items"].append(item)
            monkey["count"] += len(monkey["starting_items"])
            monkey["starting_items"] = []
    counts: list[int] = [monkey["count"] for monkey in monkeys]
    first: int
    second: int
    first, second = sorted(counts)[-2:]
    return first * second


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data: Monkeys = parse(puzzle_input)
    solution1: int = part1(data)  # Correct answer was 55216 (with my data)
    data2: Monkeys = parse(puzzle_input)
    solution2: int = part2(data2)  # Correct answer was 12848882750 (with my data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
