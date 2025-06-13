import pytest
from unittest.mock import MagicMock
from pattern_impl import *

# Тестируем базовые сценарии
def test_basic_shawarma():
    order = ShawarmaOrder()
    assert order.cost() == 500
    assert order.description() == "Основная шаурма"

def test_shawarma_with_sauce():
    order = ShawarmaOrder()
    order = SauceDecorator(order)
    assert order.cost() == 550
    assert order.description() == "Основная шаурма, Соус"
    
def test_shawarma_with_veggie():
    order = ShawarmaOrder()
    order = VeggieDecorator(order)
    assert order.cost() == 530
    assert order.description() == "Основная шаурма, Овощи"
    
def test_shawarma_with_cheese():
    order = ShawarmaOrder()
    order = CheeseDecorator(order)
    assert order.cost() == 570
    assert order.description() == "Основная шаурма, Сыр"

def test_shawarma_with_sauce_and_veggies():
    order = ShawarmaOrder()
    order = SauceDecorator(order)
    order = VeggieDecorator(order)
    assert order.cost() == 580
    assert order.description() == "Основная шаурма, Соус, Овощи"

def test_shawarma_with_all_additions():
    order = ShawarmaOrder()
    order = SauceDecorator(order)
    order = VeggieDecorator(order)
    order = CheeseDecorator(order)
    assert order.cost() == 650
    assert order.description() == "Основная шаурма, Соус, Овощи, Сыр"

# Негативные тесты: проверка некорректных данных
def test_invalid_decorator_input_none():
    with pytest.raises(TypeError):
        SauceDecorator(None)

def test_invalid_decorator_input_wrong_type():
    with pytest.raises(TypeError):
        SauceDecorator("не шаурма")

def test_sauce_decorator_with_mock():
    # Создаём мок-объект с нужными методами
    mock_order = MagicMock(spec=ShawarmaOrder)
    mock_order.cost.return_value = 500
    mock_order.description.return_value = "Тестовая шаурма"

    decorated_order = SauceDecorator(mock_order)

    # Проверяем, что итоговая цена корректна
    assert decorated_order.cost() == 550  # 500 + 50
    assert decorated_order.description() == "Тестовая шаурма, Соус"

    # Проверяем, что у мок-объекта вызвались методы
    mock_order.cost.assert_called_once()
    mock_order.description.assert_called_once()
