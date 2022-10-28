import pytest
import pizza
from dataclasses import dataclass


def test_abstract_pizza_interface():
    """Testing PizzaInterface abstract class"""
    pizza.PizzaInterface.__abstractmethods__ = set()

    @dataclass
    class Dummy(pizza.PizzaInterface):
        pass

    dummy = Dummy()
    dummy_ingredients = dummy.ingredients
    dummy_dict = dummy.dict()

    assert dummy_ingredients is None
    assert dummy_dict is None


def test_pizza_sizes_enumerator():
    """Testing PizzaSizes enumerator class"""
    pizza_sizes_dir = dir(pizza.PizzaSizes)
    assert 'S' not in pizza_sizes_dir
    assert 'M' not in pizza_sizes_dir
    assert 'XL' in pizza_sizes_dir
    assert 'L' in pizza_sizes_dir
    assert 'Large' not in pizza_sizes_dir
    assert 'ExtraLarge' not in pizza_sizes_dir


def test_pizza_constructor_empty():
    """Testing Pizza class constructor with empty object"""
    test_pizza = pizza.Pizza()
    assert test_pizza.name == 'default_pizza_name'
    assert test_pizza.size == 'Large'
    assert test_pizza._ingredients == []


def test_pizza_constructor():
    """Testing Pizza class constructor with inappropriate attributes object"""
    assert pizza.Pizza('peppe\ro\ni').name == 'peppe\ro\ni'
    assert pizza.Pizza('pepperoni' * 5).name == 'pepperoni' * 5
    assert pizza.Pizza(name='', size='M').size == 'Large'
    assert pizza.Pizza(name='', size='M' * 10).size == 'Large'
    assert pizza.Pizza(name=123).name == 'default_pizza_name'
    assert pizza.Pizza(
        'pizza',
        'XL',
        ingredients={'cheese': 1, 'more_cheese': 2}
    )._ingredients == []
    assert pizza.Pizza(
        'pizza',
        'XL',
        ingredients={'cheese', 'more_cheese'}
    )._ingredients == []
    assert pizza.Pizza(
        'pizza',
        'XL',
        ingredients={'cheese', 'more_cheese'}
    ).ingredients == ''
    assert pizza.Pizza(
        'pizza',
        'XL',
        ingredients='unknown_ingredient'
    ).ingredients == ''
    assert pizza.Pizza(
        'pizza',
        'XL',
        ingredients=12345
    ).ingredients == ''
    assert str(pizza.Pizza(name=123)) == \
           'default_pizza_name pizza, Large size'
    assert str(pizza.Pizza(size='M')) == \
           'default_pizza_name pizza, Large size'
    assert str(pizza.Pizza(size='L' * 100)) == \
           'default_pizza_name pizza, Large size'
    assert str(pizza.Pizza(size='L' * 100)) == \
           'default_pizza_name pizza, Large size'
    assert pizza.Pizza(
        'pizza',
        'XL',
        {'cheese': 1, 'more_cheese': 2}
    ).dict() == {'pizza': ''}
    assert pizza.Pizza(
        'pizza',
        'XL',
        {'cheese', 'more_cheese'},
    ).dict() == {'pizza': ''}
    assert pizza.Pizza(
        'pizza_1',
        ingredients={'cheese', 'more_cheese'},
    ) == pizza.Pizza('pizza_2', ingredients={'cheese', 'some_more_cheese'})
    assert pizza.Pizza(
        'pizza_1',
        ingredients={'cheese': 1, 'more_cheese': 2}
    ) == pizza.Pizza(
        'pizza_2',
        ingredients={'cheese': 1, 'some_more_cheese': 2}
    )
    assert pizza.Pizza('pizza_1', ingredients=12345) == \
           pizza.Pizza('pizza_2', ingredients=23456)
    assert pizza.Pizza(
        'custom pizza',
        'XL',
        ingredients=[
            'Mozarella' * 2,
            'Cheddar',
            'Pepperoni',
            'Mushrooms',
        ]
    )._ingredients == [
            'Mozarella' * 2,
            'Cheddar',
            'Pepperoni',
            'Mushrooms',
        ]


def test_margherita():
    """Testing margherita Pizza subclass."""
    assert pizza.Margherita().name == 'Margherita'
    with pytest.raises(TypeError):
        assert pizza.Margherita(name='Margherita')
    with pytest.raises(TypeError):
        assert pizza.Margherita(
            ['cheese', 'tomatoes', 'dough']
        )
    assert pizza.Margherita('M').size == 'Large'
    assert pizza.Margherita().dict() == \
           {
               'Margherita':
                   'Tomato Sauce, Mozzarella, Tomatoes'
           }
    assert str(pizza.Margherita('XL')) == \
           'Margherita pizza, Extra Large size'


def test_pepperoni():
    """Testing pepperoni Pizza subclass."""
    assert pizza.Pepperoni().name == 'Pepperoni'
    with pytest.raises(TypeError):
        assert pizza.Pepperoni(name='Pepperoni')
    with pytest.raises(TypeError):
        assert pizza.Pepperoni(
            ['cheese', 'pepperoni', 'dough']
        )
    assert pizza.Pepperoni('Standard').size == 'Large'
    assert pizza.Pepperoni().dict() == \
           {
               'Pepperoni':
                   'Tomato Sauce, Mozzarella, Pepperoni'
           }
    assert str(pizza.Pepperoni('XL')) == \
           'Pepperoni pizza, Extra Large size'


def test_hawaiian():
    """Testing hawaiian Pizza subclass."""
    assert pizza.Hawaiian().name == 'Hawaiian'
    with pytest.raises(TypeError):
        assert pizza.Hawaiian(name='Hawaiian')
    with pytest.raises(TypeError):
        assert pizza.Hawaiian(
            ['cheese', 'chicken', 'pineapple']
        )
    assert pizza.Hawaiian('Small').size == 'Large'
    assert pizza.Hawaiian().dict() == \
           {
               'Hawaiian':
                   'Tomato Sauce, Mozzarella, Chicken, Pineapples'
           }
    assert str(pizza.Pepperoni('XL')) == \
           'Pepperoni pizza, Extra Large size'


if __name__ == "__main__":
    pytest.main()  # pragma: no cover
