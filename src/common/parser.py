# src/common/parser.py


def parse_input(file_path: str) -> tuple[list[int], list[int]]:
    list_a, list_b = [], []
    with open(file_path, "r") as file:
        for line_num, line in enumerate(file, 1):
            line = line.strip()
            if not line:  # Skip empty lines
                continue

            try:
                parts = line.split()
                if len(parts) != 2:
                    raise ValueError(
                        f"Line {line_num}: Expected exactly "
                        f"2 space-separated integers, "
                        f"got {len(parts)} values"
                    )

                try:
                    a = int(parts[0])
                    b = int(parts[1])
                except ValueError as e:
                    raise ValueError(
                        f"Line {line_num}: Unable to convert "
                        f"values to integers: '{line}'"
                    ) from e

                list_a.append(a)
                list_b.append(b)

            except ValueError as e:
                raise ValueError(f"Error parsing input file: {str(e)}") from e

    return list_a, list_b
