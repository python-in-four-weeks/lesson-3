import pytest
from pytest_mock import MockerFixture
from freezegun import freeze_time

import random
from datetime import date
from math import isclose
from io import StringIO

import challenges


@pytest.mark.parametrize('random_seed, expected_coin_side_sequence', [
    (10, ['heads', 'tails', 'tails', 'heads', 'heads']),
    (20, ['heads', 'tails', 'heads', 'tails', 'heads']),
])
def test_flip_coin(
        random_seed: int,
        expected_coin_side_sequence: list[challenges.CoinSide]) -> None:
    random.seed(random_seed)
    coin_side_sequence = [challenges.flip_coin() for _ in range(5)]
    assert coin_side_sequence == expected_coin_side_sequence, f"A random seed of {random_seed} should generate the sequence {expected_coin_side_sequence}"


@pytest.mark.parametrize('random_seed, dice_sides, expected_dice_roll_sequence', [
    (10, 1, [1, 1, 1, 1, 1]),
    (20, 6, [6, 6, 2, 3, 6]),
])
def test_roll_n_sided_dice_with_valid_number_of_sides(
        random_seed: int,
        dice_sides: int,
        expected_dice_roll_sequence: list[challenges.CoinSide]) -> None:
    random.seed(random_seed)
    dice_roll_sequence = [challenges.roll_n_sided_dice(dice_sides) for _ in range(5)]
    assert dice_roll_sequence == expected_dice_roll_sequence, f"A random seed of {random_seed} should generate the sequence {expected_dice_roll_sequence}"


@pytest.mark.parametrize('dice_sides, expected_error_message', [
    (-4, "It isn't possible to have a -4-sided dice"),
    (0, "It isn't possible to have a 0-sided dice"),
])
def test_roll_n_sided_dice_with_invalid_number_of_sides(
        dice_sides: int,
        expected_error_message: str) -> None:
    with pytest.raises(ValueError) as exception:
        challenges.roll_n_sided_dice(dice_sides)
    assert str(exception.value) == expected_error_message, f"A {dice_sides}-sided dice should generate the error message \"{expected_error_message}\""


@pytest.mark.parametrize('date_today, date_in_two_weeks', [
    (date(2021, 10, 8), date(2021, 10, 22)),
    (date(2022, 4, 27), date(2022, 5, 11)),
])
def test_get_renewed_return_date(
        date_today: date,
        date_in_two_weeks: date) -> None:
    with freeze_time(date_today):
        mock_renewed_return_date = challenges.get_renewed_return_date()
    renewed_return_date = date(mock_renewed_return_date.year, mock_renewed_return_date.month, mock_renewed_return_date.day)
    assert renewed_return_date == date_in_two_weeks, f"If today is {date_today}, the renewed return date should be {date_in_two_weeks}"


@pytest.mark.parametrize('date_today, date_of_birth, expected_age', [
    (date(2008, 1, 1), date(2008, 1, 1), {'years': 0, 'months': 0}),
    (date(2009, 11, 12), date(2009, 5, 11), {'years': 0, 'months': 6}),
    (date(2010, 6, 5), date(2010, 3, 20), {'years': 0, 'months': 2}),
    (date(2012, 10, 7), date(2011, 4, 5), {'years': 1, 'months': 6}),
    (date(2016, 2, 8), date(2012, 9, 30), {'years': 3, 'months': 4}),
    (date(2000, 7, 24), date(1900, 7, 25), {'years': 99, 'months': 11}),
])
def test_calculate_age_with_valid_date_of_birth(
        date_today: date,
        date_of_birth: date,
        expected_age: challenges.Age) -> None:
    with freeze_time(date_today):
        age = challenges.calculate_age(date_of_birth)
    assert age == expected_age, f"If today is {date_today} and the date of birth is {date_of_birth}, the age should be {expected_age}"


@pytest.mark.parametrize('date_today, date_of_birth, expected_error_message', [
    (date(2008, 1, 1), date(2008, 1, 2), "It isn't possible to have a date of birth in the future"),
])
def test_calculate_age_with_invalid_date_of_birth(
        date_today: date,
        date_of_birth: date,
        expected_error_message: str) -> None:
    with freeze_time(date_today):
        with pytest.raises(ValueError) as exception:
            challenges.calculate_age(date_of_birth)
    assert str(exception.value) == expected_error_message, f"A date of birth in the future should generate the error message \"{expected_error_message}\""


@pytest.mark.parametrize('radius, expected_volume', [
    (0, 0),
    (2, 33.510321638291124),
    (2.8794119114848606, 100),
])
def test_calculate_sphere_volume_with_valid_radius(
        radius: float,
        expected_volume: float) -> None:
    volume = challenges.calculate_sphere_volume(radius)
    assert isclose(volume, expected_volume), f"A sphere of radius {radius} should have volume {expected_volume}"


@pytest.mark.parametrize('radius, expected_error_message', [
    (-1, "It isn't possible for a sphere to have a negative radius"),
])
def test_calculate_sphere_volume_with_invalid_radius(
        radius: float,
        expected_error_message: str) -> None:
    with pytest.raises(ValueError) as exception:
        challenges.calculate_sphere_volume(radius)
    assert str(exception.value) == expected_error_message, f"A negative radius should generate the error message \"{expected_error_message}\""


@pytest.mark.parametrize('a, b, c, expected_solutions', [
    (4, -9, -28, frozenset({-1.75, 4})),
    (1, -8, 15, frozenset({3, 5})),
    (1, 12, 0, frozenset({0, -12})),
    (4, 0, -25, frozenset({-2.5, 2.5})),
    (2, 0, 0, frozenset({0})),
    (0, 2, -3, frozenset({1.5})),
    (0, 5, 0, frozenset({0})),
    (0, 0, 1, frozenset()),
    (7, -3, 2, frozenset()),
])
def test_calculate_quadratic_equation_solutions_with_finite_solutions(
        a: float,
        b: float,
        c: float,
        expected_solutions: frozenset[float]) -> None:
    solutions = challenges.calculate_quadratic_equation_solutions(a, b, c)
    assert solutions == expected_solutions, f"{a}x² + {b}x + {c} = 0 should have solutions {expected_solutions}"


@pytest.mark.parametrize('a, b, c, expected_error_message', [
    (0, 0, 0, "Infinite number of solutions found"),
])
def test_calculate_quadratic_equation_solutions_with_infinite_solutions(
        a: float,
        b: float,
        c: float,
        expected_error_message: str) -> None:
    with pytest.raises(ValueError) as exception:
        challenges.calculate_quadratic_equation_solutions(a, b, c)
    assert str(exception.value) == expected_error_message, f"{a}x² + {b}x + {c} = 0 should generate the error message \"{expected_error_message}\""


@pytest.mark.parametrize('guest_count_input, expected_guest_count', [
    ('5', 5),
    ('1', 1),
])
def test_get_guest_count_with_valid_count(
        mocker: MockerFixture,
        guest_count_input: str,
        expected_guest_count: int) -> None:
    mocker.patch('builtins.input', side_effect=[guest_count_input])
    guest_count = challenges.get_guest_count()
    assert guest_count == expected_guest_count, f"An input of \"{guest_count_input}\" should correspond to a guest count of {expected_guest_count}"


@pytest.mark.parametrize('guest_count_input, expected_error_message', [
    ('-1', "Bookings cannot be for a negative number of guests"),
    ('0', "Bookings cannot be for zero guests"),
    ('1.5', "Bookings must be for a valid whole number of guests"),
    ('-2.5', "Bookings must be for a valid whole number of guests"),
    ('hello', "Bookings must be for a valid whole number of guests"),
])
def test_get_guest_count_with_invalid_count(
        mocker: MockerFixture,
        guest_count_input: str,
        expected_error_message: str) -> None:
    mocker.patch('builtins.input', side_effect=[guest_count_input])
    with pytest.raises(ValueError) as exception:
        challenges.get_guest_count()
    assert str(exception.value) == expected_error_message, f"An input of \"{guest_count_input}\" should generate the error message \"{expected_error_message}\""


@pytest.mark.parametrize('guest_count_input, expected_output', [
    ('3', "That will be 33.33 each, thank you!"),
    ('1', "That will be 100.00 each, thank you!"),
    ('-1', "The bill cannot be split between a negative number of guests."),
    ('0', "The bill cannot be split between zero guests."),
    ('1.5', "That isn't a valid whole number of guests."),
    ('-2.5', "That isn't a valid whole number of guests."),
    ('hello', "That isn't a valid whole number of guests."),
])
def test_split_bill_evenly(
        mocker: MockerFixture,
        guest_count_input: str,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[guest_count_input])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.split_bill_evenly()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 0, "There doesn't seem to be any output"
    assert len(outputted_lines) < 2, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"An input of \"{guest_count_input}\" should generate the output \"{expected_output}\""


@pytest.mark.parametrize('selected_option_number, expected_output', [
    ('0', "You selected: Purchase some fruit."),
    ('2', "You selected: Just have a browse."),
    ('4', "That wasn't one of the options."),
    ('hello', "That wasn't one of the options."),
])
def test_greet_customer(
        mocker: MockerFixture,
        selected_option_number: str,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[selected_option_number])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.greet_customer()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 4, "There doesn't seem to be any output"
    assert len(outputted_lines) < 6, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"An input of \"{selected_option_number}\" should generate the output \"{expected_output}\""


@pytest.mark.parametrize('selected_fruit, expected_output', [
    ('orange', "That will be 1.24, please!"),
    ('apple', "That will be 0.95, please!"),
    ('banana', "That wasn't one of the options."),
])
def test_serve_customer(
        mocker: MockerFixture,
        selected_fruit: str,
        expected_output: str) -> None:
    mocker.patch('builtins.input', side_effect=[selected_fruit])
    mock_stdout = mocker.patch('sys.stdout', new_callable=StringIO)
    challenges.serve_customer()
    outputted_lines = mock_stdout.getvalue().splitlines()
    assert len(outputted_lines) > 3, "There doesn't seem to be any output"
    assert len(outputted_lines) < 5, "There seem to be too many printed lines"
    assert outputted_lines[-1] == expected_output, f"An input of \"{selected_fruit}\" should generate the output \"{expected_output}\""
