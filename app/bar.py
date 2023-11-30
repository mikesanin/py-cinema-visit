from __future__ import annotations


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name


class CinemaBar:
    @staticmethod
    def sell_product(customer: Customer, product: str) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
