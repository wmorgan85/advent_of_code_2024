import os
import tempfile

import pytest

from day_01.part1 import parse_input, solve


def test_parse_input_valid_data():
    # Arrange
    test_content = "10\t20\n30\t40\n50\t60"
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(test_content)
        temp_file.close()

    # Act
    list_a, list_b = parse_input(temp_file.name)

    # Assert
    assert list_a == [10, 30, 50]
    assert list_b == [20, 40, 60]

    # Cleanup
    os.unlink(temp_file.name)


@pytest.mark.parametrize(
    "file_content,expected_a,expected_b",
    [
        pytest.param("0\t0", [0], [0], id="single_zero_pair"),
        pytest.param("-1\t-2", [-1], [-2], id="negative_numbers"),
        pytest.param(
            "100\t200\n300\t400",
            [100, 300],
            [200, 400],
            id="multiple_pairs",
        ),
    ],
)
def test_parse_input_various_inputs(file_content, expected_a, expected_b):
    # Arrange
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(file_content)
        temp_file.close()

    # Act
    list_a, list_b = parse_input(temp_file.name)

    # Assert
    assert list_a == expected_a
    assert list_b == expected_b

    # Cleanup
    os.unlink(temp_file.name)


def test_parse_input_empty_file():
    # Arrange
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.close()

    # Act
    list_a, list_b = parse_input(temp_file.name)

    # Assert
    assert list_a == []
    assert list_b == []

    # Cleanup
    os.unlink(temp_file.name)


def test_parse_input_file_not_found():
    # Act & Assert
    with pytest.raises(FileNotFoundError):
        parse_input("nonexistent_file.txt")


def test_parse_input_invalid_format():
    # Arrange
    test_content = "10\t20\n30"  # Missing second value
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as temp_file:
        temp_file.write(test_content)
        temp_file.close()

    # Act & Assert
    with pytest.raises(ValueError):
        parse_input(temp_file.name)

    # Cleanup
    os.unlink(temp_file.name)


@pytest.mark.parametrize(
    "list_one,list_two,expected",
    [
        pytest.param([1, 2, 3], [4, 5, 6], 9, id="increasing_sequences"),
        pytest.param([3, 2, 1], [6, 5, 4], 9, id="decreasing_sequences"),
        pytest.param([1, 1, 1], [2, 2, 2], 3, id="uniform_sequences"),
        pytest.param([-1, 0, 1], [1, 0, -1], 0, id="mixed_sign_sequences"),
        pytest.param([0, 0, 0], [0, 0, 0], 0, id="zero_sequences"),
    ],
)
def test_solve_happy_path(list_one, list_two, expected):
    # Act
    result = solve(list_one, list_two)

    # Assert
    assert result == expected


def test_solve_empty_lists():
    # Act
    result = solve([], [])

    # Assert
    assert result == 0


def test_solve_single_element_lists():
    # Act
    result = solve([5], [10])

    # Assert
    assert result == 5


@pytest.mark.parametrize(
    "list_one,list_two",
    [
        pytest.param([1, 2], [1, 2, 3], id="different_lengths_first_shorter"),
        pytest.param([1, 2, 3], [1, 2], id="different_lengths_second_shorter"),
    ],
)
def test_solve_different_list_lengths(list_one, list_two):
    # Act & Assert
    with pytest.raises(ValueError, match="Lists must have the same length."):
        solve(list_one, list_two)
