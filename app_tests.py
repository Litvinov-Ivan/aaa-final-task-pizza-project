import pytest
import app
import pizza
from click.testing import CliRunner


def test_log_func_empty():
    """Testing log decorator with empty function"""
    @app.log()
    def to_be_decorated():
        pass

    with pytest.raises(IndexError):
        to_be_decorated()


def test_log_func_wrong_input():
    """Testing log decorator with wrong input"""
    @app.log()
    def to_be_decorated(pizza_argument=(1, 2, 3)):
        pass

    with pytest.raises(IndexError):
        to_be_decorated()


def test_log_incorrect_pattern():
    """Testing log decorator with incorrect pattern"""
    @app.log(123)
    def to_be_decorated(pizza_argument):
        pass

    with pytest.raises(AttributeError):
        to_be_decorated()


def test_log_pattern_string_1():
    """Testing log decorator with pattern"""
    @app.log('pizzaname' * 2)
    def to_be_decorated(pizza_argument):
        pass

    assert str(to_be_decorated(pizza.Pizza('test_pizza'))) == 'test_pizza' * 2


def test_log_pattern_string_2():
    """Testing log decorator with parenthesis pattern"""
    @app.log('{}' * 5)
    def to_be_decorated(pizza_argument):
        pass

    assert str(to_be_decorated(pizza.Pizza('test_pizza'))).isnumeric()


def test_bake_func():
    """Testing bake function"""
    assert app.bake(
        pizza.Pizza('test_pizza')
    ).startswith('👨‍🍳 Приготовили test_pizza за')


def test_delivery_func():
    """Testing delivery function"""
    assert app.delivery_func(
        pizza.Pizza('test_pizza')
    ).startswith('🛵 Доставили test_pizza за')


def test_pickup_func():
    """Testing pickup function"""
    assert app.pickup(
        pizza.Pizza('test_pizza')
    ).startswith('🏠 Забрали test_pizza за')


def test_menu():
    """Testing menu function"""
    runner = CliRunner()
    result = runner.invoke(app.menu)
    assert result.exit_code == 0
    assert result.output == \
           '- Margherita 🧀: Tomato Sauce, Mozzarella, Tomatoes\n'\
           '- Pepperoni 🍕: Tomato Sauce, Mozzarella, Pepperoni\n'\
           '- Hawaiian 🍍: Tomato Sauce, Mozzarella, Chicken, Pineapples\n'


def test_order():
    """Testing order function"""
    runner = CliRunner()
    order_test_1 = runner.invoke(
        app.order,
        ['pizza_name_order', '--delivery', '--size', 'XL']
    )
    order_test_2 = runner.invoke(
        app.order,
        ['hawaiian', '--size', 'M']
    )
    assert order_test_1.exit_code == 0
    assert order_test_1.output.startswith(
        '🧾 Сделан заказ на: Pizza_name_order pizza, Extra Large size\n'
        '👨\u200d🍳 Приготовили Pizza_name_order за'
    )
    assert order_test_2.exit_code == 0
    assert order_test_2.output.startswith(
        'It is either L or XL sizes, pizza size will be set to Large\n'
        '🧾 Сделан заказ на: Hawaiian pizza, Large size\n'
        '👨\u200d🍳 Приготовили Hawaiian за'
    )


if __name__ == "__main__":
    pytest.main()
