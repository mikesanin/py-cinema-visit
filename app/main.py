from typing import Dict, List

from app.сinema.bar import CinemaBar
from app.сinema.hall import CinemaHall
from app.people.customer import Customer


def cinema_visit(customers: List[Dict[str, str]], hall_number: int, cleaner: str, movie_name=None) -> None:
    cinema_bar = CinemaBar()
    cinema_hall = CinemaHall(hall_number)

    customer_objects = []
    for customer_info in customers:
        customer = Customer(customer_info["name"], customer_info["food"])
        customer_objects.append(customer)
        cinema_bar.sell_product(customer.food, customer)

    cinema_hall.movie_session(movie_name, customer_objects, cleaner)
