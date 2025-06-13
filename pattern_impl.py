# pattern_impl.py

class ShawarmaOrder:
    def cost(self):
        return 500  # Базовая цена шаурмы

    def description(self):
        return "Основная шаурма"


def check_shawarma_order(shawarma_order):
    """Функция для рекурсивной проверки типа."""
    if isinstance(shawarma_order, ShawarmaOrder):
        return True
    if hasattr(shawarma_order, '_shawarma_order'):
        return check_shawarma_order(shawarma_order._shawarma_order)
    return False


class SauceDecorator:
    def __init__(self, shawarma_order):
        if not check_shawarma_order(shawarma_order):  # Проверка типа
            raise TypeError("Передан некорректный параметр, ожидался объект типа ShawarmaOrder")
        self._shawarma_order = shawarma_order

    def cost(self):
        return self._shawarma_order.cost() + 50  # Цена соуса

    def description(self):
        return self._shawarma_order.description() + ", Соус"


class VeggieDecorator:
    def __init__(self, shawarma_order):
        if not check_shawarma_order(shawarma_order):  # Проверка типа
            raise TypeError("Передан некорректный параметр, ожидался объект типа ShawarmaOrder")
        self._shawarma_order = shawarma_order

    def cost(self):
        return self._shawarma_order.cost() + 30  # Цена овощей

    def description(self):
        return self._shawarma_order.description() + ", Овощи"


class CheeseDecorator:
    def __init__(self, shawarma_order):
        if not check_shawarma_order(shawarma_order):  # Проверка типа
            raise TypeError("Передан некорректный параметр, ожидался объект типа ShawarmaOrder")
        self._shawarma_order = shawarma_order

    def cost(self):
        return self._shawarma_order.cost() + 70  # Цена сыра

    def description(self):
        return self._shawarma_order.description() + ", Сыр"

