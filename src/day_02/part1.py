from common.parser import parse_multi_value_per_line
from common.script_path import get_caller_file_path as get_local_path

def is_report_safe(report: list[int]) -> bool:

    all_increasing = all(report[i] < report[i+1] for i in range(len(report)-1))
    all_decreasing = all(report[i] > report[i+1] for i in range(len(report)-1))

    if all_increasing or all_decreasing:
        return all(1 <= abs(next_item - current) <= 3 
            for current, next_item in zip(report, report[1:]))
    
    return False

def run_test():        
    test_data = [
        [7,6,4,2,1],
        [1,2,7,8,9],
        [9,7,6,2,1],
        [1,3,2,4,5],
        [8,6,4,4,1],
        [1,3,6,7,9],
    ]

    for report in test_data:
        print(f"{report=} {is_report_safe(report)=}")

    print(f"{sum(is_report_safe(report) for report in test_data)=}")


def run():
    input_file = get_local_path("input.txt")
    data = parse_multi_value_per_line(input_file)
    return sum(is_report_safe(report) for report in data)

if __name__ == "__main__":
    print("Day 2, Part 1:", run())