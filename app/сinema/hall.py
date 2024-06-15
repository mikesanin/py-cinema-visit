from __future__ import annotations

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def clean_hall(number):
    pass


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, cleaning_staff: Cleaner, customers: list) -> None:
        print("{movie_name} started in hall number {self.number}.")
        for customer in customers:
            customer.watch_movie(movie_name)
        print('"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
