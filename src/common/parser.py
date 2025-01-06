from typing import List, Tuple

def _parse_line(line_num: int, line: str) -> List[int]:
    try:
        return [int(part) for part in line.split()]
    except ValueError as e:
        raise ValueError(f"Line {line_num}: Invalid integers: '{line}'") from e

def parse_input(file_path: str) -> Tuple[List[int], List[int]]:
    list_a, list_b = [], []
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue

            try:
                parts = _parse_line(line_num, line)
                if len(parts) != 2:
                    raise ValueError(f"Line {line_num}: Expected 2 integers, got {len(parts)}")
                list_a.append(parts[0])
                list_b.append(parts[1])
            except ValueError as e:
                raise ValueError(f"Error parsing input file: {str(e)}") from e

    return list_a, list_b

def parse_multi_value_per_line(file_path: str) -> List[List[int]]:
    result = []
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, 1):
            if not line.strip():
                continue
            try:
                result.append(_parse_line(line_num, line))
            except ValueError as e:
                raise ValueError(f"Error parsing input file: {str(e)}") from e

    return result

