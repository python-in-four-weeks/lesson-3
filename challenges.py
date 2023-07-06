from typing import Literal, TypedDict
from datetime import date


CoinSide = Literal['heads', 'tails']


class Age(TypedDict):
    years: int
    months: int


def flip_coin() -> CoinSide:
    return 'heads'


def roll_n_sided_dice(n: int) -> int:
    return 0


def get_renewed_return_date() -> date:
    return date.today()


def calculate_age(date_of_birth: date) -> Age:
    return {
        'years': 0,
        'months': 0,
    }


def calculate_sphere_volume(radius: float) -> float:
    return 0.0


def calculate_quadratic_equation_solutions(a: float, b: float, c: float) -> frozenset[float]:
    return frozenset()


def get_guest_count() -> int:
    return 0


def split_bill_evenly() -> None:
    pass


def greet_customer() -> None:
    options = ['Purchase some fruit', 'Find out more about the fruit we sell', 'Just have a browse']
    print("Welcome to the greengrocer's store! Your options:")
    for index, option in enumerate(options):
        print(f"{index}. {option}")
    chosen_option = input("Which option will you choose? Type its number: ")
    print(f"You selected: {options[int(chosen_option)]}.")


def serve_customer() -> None:
    fruit_prices = {'orange': 1.24, 'apple': 0.95}
    print("We're glad you'd like to purchase some fruit. Here are the fruits we sell and their prices:")
    for fruit, price in fruit_prices.items():
        print(f"- Each {fruit}: {price}")
    chosen_fruit = input("Which fruit would you like? ").casefold()
    print(f"That will be {fruit_prices[chosen_fruit]}, please!")


if __name__ == '__main__':
    # Try out your functions here
    pass
