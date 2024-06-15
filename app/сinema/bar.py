from __future__ import annotations


class Customer:
    pass


class CinemaBar:
    @staticmethod
    def sell_product(product: str, customer=None) -> None:
        print(f"Cinema bar sold {product} to {customer.name}.")
